#!/usr/bin/env python3
"""Convertit les notes exportées de Nimbus Note (note.html) en Markdown.

Usage :
  python3 convert_nimbus.py SOURCE DEST [--only TEXTE ...]

  SOURCE : dossier du kit (ex. .../KIT DE SURVIE APPS STATIQUES)
  DEST   : dossier de sortie (ex. .../KITS_SURVIE/notes/apps-statiques)
  --only : ne convertit que les notes dont le chemin contient TEXTE
"""
import sys, re, json, shutil, unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, quote

COURS = 'apps-statiques'
VOID = {'br', 'img', 'hr', 'meta', 'link', 'input', 'source', 'col', 'wbr'}
LANG = {'html': 'html', 'xml': 'html', 'css': 'css', 'javascript': 'javascript',
        'js': 'javascript', 'json': 'json', 'php': 'php', 'sql': 'sql',
        'bash': 'bash', 'shell': 'bash', 'scss': 'scss', 'vue': 'html'}


def slug(s):
    s = re.sub(r'\(Conflit[^)]*\)', '', s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:70].strip('-')


def yq(s):
    """Guillemets YAML uniquement si nécessaire."""
    return json.dumps(s, ensure_ascii=False) if re.search(r'[:#"\'\[\]{}&*!|>%@`]', s) or s != s.strip() else s


class Conv(HTMLParser):
    def __init__(self, asset_cb):
        super().__init__(convert_charrefs=True)
        self.asset_cb = asset_cb
        self.blocks, self.stack, self.buf = [], [], []
        self.title, self.in_title, self.skip = '', False, 0
        self.code = None
        self.in_label = self.in_pre = self.in_code_inline = self.in_filename = 0
        self.file = None
        self.table = self.row = None
        self.counters, self.labels = {}, set()

    # ---------- utilitaires
    def add(self, kind, text):
        if text:
            self.blocks.append((kind, text))

    def take(self):
        t = ''.join(self.buf)
        self.buf = []
        t = re.sub(r'[ \t]+', ' ', t)
        t = re.sub(r' ?\n ?', '\n', t).strip()
        return t.replace('\n', '  \n')

    def flush_stray(self):
        self.add('p', self.take())

    def emit_code(self):
        c, self.code = self.code, None
        label = c['label'].strip()
        self.labels.add(label or '(vide)')
        text = c['text'].strip('\n').rstrip()
        if text.strip():
            self.add('code', '```' + LANG.get(label.lower().split('/')[0].strip(), '') + '\n' + text + '\n```')

    def emit_table(self):
        rows = [r for r in (self.table or []) if r]
        self.table = None
        if not rows:
            return
        n = max(len(r) for r in rows)
        rows = [r + [''] * (n - len(r)) for r in rows]
        lines = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * n]
        lines += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
        self.add('table', '\n'.join(lines))

    # ---------- balises ouvrantes
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        if tag == 'title':
            self.in_title = True
            return
        if tag in VOID:
            return self.start_void(tag, a, cls)
        role = data = None
        if self.skip:
            pass
        elif tag in ('svg', 'style', 'script') or (tag == 'div' and 'outline' in cls):
            role = 'skip'
            self.skip += 1
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5'):
            self.flush_stray(); role, data = 'heading', int(tag[1])
        elif tag == 'blockquote':
            self.flush_stray(); role = 'quote'
        elif tag == 'li' and 'list-item' in cls:
            self.flush_stray()
            m = re.search(r'indent-(\d+)', ' '.join(cls))
            role, data = 'li', ('list-item-number' in cls, int(m.group(1)) if m else 0)
        elif tag in ('ul', 'ol'):
            self.counters = {}
        elif tag == 'div' and 'syntax-wrapper' in cls:
            self.flush_stray(); role = 'syntax'
            self.code = {'label': '', 'text': ''}
        elif tag == 'span' and 'syntax-control-label' in cls:
            role = 'label'; self.in_label += 1
        elif tag == 'pre':
            role = 'pre'; self.in_pre += 1
            if self.code is None:
                self.code = {'label': '', 'text': '', 'own': True}
        elif tag == 'div' and 'file' in cls:
            self.flush_stray(); role = 'file'
            self.file = {'name': '', 'href': ''}
        elif tag == 'span' and 'file-name' in cls:
            role = 'fname'; self.in_filename += 1
        elif tag == 'table':
            self.flush_stray(); role = 'table'; self.table = []
        elif tag == 'tr':
            role = 'row'; self.row = []
        elif tag in ('td', 'th'):
            role, data = 'cell', self.buf
            self.buf = []
        elif 'attachment-caption' in cls:
            self.flush_stray(); role = 'caption'
        elif tag == 'div' and 'editable-text' in cls and 'paragraph' in cls and self.row is None:
            self.flush_stray(); role = 'para'
        elif tag == 'iframe':
            self.flush_stray()
            src = a.get('src', '')
            m = re.search(r'youtube\.com/embed/([\w-]+)', src)
            url = f'https://www.youtube.com/watch?v={m.group(1)}' if m else src
            self.add('p', f'▶️ [Vidéo]({url})')
        elif not self.in_pre:
            marker = {'strong': '**', 'b': '**', 'em': '*', 'i': '*', 's': '~~', 'del': '~~'}.get(tag)
            if tag == 'code':
                marker = '`'; self.in_code_inline += 1
            if tag == 'a':
                marker = 'a'
                href = a.get('href', '')
                if self.file is not None:
                    self.file['href'] = self.asset_cb(href)
                    href = ''
                elif href.startswith('#'):
                    href = ''
                else:
                    href = self.asset_cb(href)
                data = (marker, len(self.buf), href)
            elif marker:
                data = (marker, len(self.buf), '')
            if marker:
                role = 'inline'
        self.stack.append([tag, role, data])

    def start_void(self, tag, a, cls):
        if self.skip:
            return
        if tag == 'br':
            if 'separator' not in cls and not self.in_pre:
                self.buf.append('\n')
        elif tag == 'img':
            new = self.asset_cb(a.get('src', ''))
            md = f"![{a.get('alt', '')}]({new})"
            if self.row is not None:
                self.buf.append(md)
            else:
                self.flush_stray(); self.add('img', md)
        elif tag == 'hr':
            self.flush_stray(); self.add('hr', '---')

    # ---------- balises fermantes
    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            return
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                break
        else:
            return
        while len(self.stack) > i:
            self.close(self.stack.pop())

    def close(self, entry):
        tag, role, data = entry
        if role == 'skip':
            self.skip -= 1
        elif role == 'heading':
            t = self.take()
            self.add('h', '#' * min(data + 1, 6) + ' ' + t if t else '')
        elif role == 'para':
            t = self.take()
            if not self.blocks and t.strip('*').startswith('KIT DE SURVIE'):
                return
            self.add('p', t)
        elif role == 'quote':
            t = self.take()
            self.add('q', '> ' + t.replace('\n', '\n> ') if t else '')
        elif role == 'caption':
            t = self.take()
            self.add('p', f'*{t}*' if t else '')
        elif role == 'li':
            t = self.take()
            ordered, indent = data
            if ordered:
                self.counters[indent] = self.counters.get(indent, 0) + 1
            mark = f'{self.counters[indent]}. ' if ordered else '- '
            self.add('li', '    ' * indent + mark + t if t else '')
        elif role == 'label':
            self.in_label -= 1
        elif role == 'pre':
            self.in_pre -= 1
            if self.code and self.code.get('own'):
                self.emit_code()
        elif role == 'syntax':
            if self.code:
                self.emit_code()
        elif role == 'fname':
            self.in_filename -= 1
        elif role == 'file':
            f, self.file = self.file, None
            name = f['name'].strip()
            self.add('p', '📎 ' + (f"[{name}]({f['href']})" if f['href'] else name) if name else '')
        elif role == 'cell':
            t = re.sub(r'\s+', ' ', ''.join(self.buf).replace('\n', '<br>')).strip()
            self.row.append(t.replace('|', '\\|'))
            self.buf = data
        elif role == 'row':
            if self.table is not None:
                self.table.append(self.row)
            self.row = None
        elif role == 'table':
            self.emit_table()
        elif role == 'inline':
            marker, start, href = data
            if marker == '`':
                self.in_code_inline -= 1
            seg = ''.join(self.buf[start:])
            core = seg.strip()
            if core and (marker != 'a' or href):
                lead = seg[:len(seg) - len(seg.lstrip())]
                trail = seg[len(seg.rstrip()):]
                wrapped = f'[{core}]({href})' if marker == 'a' else marker + core + marker
                self.buf[start:] = [lead + wrapped + trail]

    # ---------- texte
    def handle_data(self, d):
        if self.in_title:
            self.title += d
            return
        if self.skip:
            return
        if self.code is not None:
            if self.in_label:
                self.code['label'] += d
            elif self.in_pre:
                self.code['text'] += d
            return
        if self.file is not None:
            if self.in_filename:
                self.file['name'] += d
            return
        d = re.sub(r'\s+', ' ', d)
        if not self.in_code_inline:
            d = d.replace('<', '&lt;')
        self.buf.append(d)

    def finish(self):
        self.flush_stray()
        while self.stack:
            self.close(self.stack.pop())
        self.flush_stray()


def render(blocks):
    out, prev = [], None
    for kind, text in blocks:
        if out:
            out.append('\n' if kind == 'li' and prev == 'li' else '\n\n')
        out.append(text)
        prev = kind
    return ''.join(out) + '\n'


def atelier_info(name):
    m = re.match(r'ATELIER\s*(\d+)\s*!?\s*(.*)', name, re.I)
    n, label = (int(m.group(1)), m.group(2)) if m else (99, name)
    return n, label.strip(), f'{n:02d}-{slug(label)}'


def convert(note_html, out_dir, atelier_n, atelier_label, order):
    src_dir, copied, warns = note_html.parent, [], []

    def asset_cb(ref):
        if not ref or ref.startswith(('http:', 'https:', 'data:', 'mailto:', '#')):
            return ref
        f = src_dir / unquote(ref.split('?')[0]).removeprefix('./')
        if f.is_file():
            dst = out_dir / 'images' / f.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
            copied.append(f.name)
            return 'images/' + quote(f.name)
        warns.append('ressource introuvable : ' + ref)
        return ref

    p = Conv(asset_cb)
    p.feed(note_html.read_text(encoding='utf-8'))
    p.finish()
    title = re.sub(r'\s*\(Conflit[^)]*\)', '', p.title).strip() or note_html.parent.name
    bare = re.sub(r'^\s*(AT-)?\d+([.\-]\d+)*\s*[.\-]?\s*', '', title)
    fm = ['---', f'titre: {yq(title)}', f'cours: {COURS}', f'atelier: {atelier_n}',
          f'atelier_titre: {yq(atelier_label)}', f'ordre: {order}', '---', '', f'# {title}', '']
    md_path = out_dir / f'{order:02d}-{slug(bare)}.md'
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path.write_text('\n'.join(fm) + '\n' + render(p.blocks), encoding='utf-8')
    kinds = Counter(k for k, _ in p.blocks)
    return md_path, kinds, len(set(copied)), p.labels, warns


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    src, dst = Path(args[0]), Path(args[1])
    only = args[args.index('--only') + 1:] if '--only' in args else []
    groups = {}
    for f in sorted(src.glob('*/*/note.html')):
        groups.setdefault(f.parent.parent.name, []).append(f)
    total = Counter()
    for aname in sorted(groups, key=lambda x: atelier_info(x)[0]):
        n, label, aslug = atelier_info(aname)
        for order, f in enumerate(sorted(groups[aname], key=lambda x: x.parent.name), 1):
            rel = str(f.relative_to(src))
            if only and not any(o in rel for o in only):
                continue
            md, kinds, nimg, labels, warns = convert(f, dst / aslug, n, label, order)
            total.update(kinds)
            print(f'OK  {md.relative_to(dst)}  | blocs: {dict(kinds)} | fichiers copiés: {nimg} | code: {sorted(labels)}')
            for w in warns:
                print('    ATTENTION', w)
    print('TOTAL blocs :', dict(total))


if __name__ == '__main__':
    main()

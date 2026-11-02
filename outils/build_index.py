#!/usr/bin/env python3
"""Génère notes/index.json (sommaire) et notes/search.json (recherche plein texte).

Usage : python3 outils/build_index.py
À relancer après chaque ajout ou renommage de note.
"""
import re, json
from pathlib import Path

NOTES = Path(__file__).resolve().parent.parent / 'notes'
COURS = {'apps-statiques': 'Apps statiques'}
SIGLES = 'HTML CSS HTTP JS UI UX DOM SQL PHP SEO XML URL SVG JSON API CMS WEB'.split()
CORRECTIONS = {'Mementos': 'Mémentos'}


def phrase(titre):
    """MAJUSCULES -> Phrase, en gardant les sigles."""
    if titre != titre.upper():
        return titre
    t = titre.lower().capitalize()
    t = re.sub(r'\b(' + '|'.join(SIGLES) + r')(\d*)\b', lambda m: m.group(1).upper() + m.group(2), t, flags=re.I)
    return CORRECTIONS.get(t, t)


def lire(md):
    texte = md.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n(.*)', texte, re.S)
    meta, corps = {}, texte
    if m:
        corps = m.group(2)
        for ligne in m.group(1).splitlines():
            k, _, v = ligne.partition(':')
            v = v.strip()
            meta[k.strip()] = json.loads(v) if v.startswith('"') else v
    return meta, corps


def brut(corps):
    t = re.sub(r'<video.*?</video>', ' ', corps, flags=re.S)
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'[#>*`|]|^-{3,}$|^\s*(?:-|\d+\.)\s', ' ', t, flags=re.M)
    return re.sub(r'\s+', ' ', t).strip()


index, recherche = [], []
for dossier_cours in sorted(p for p in NOTES.iterdir() if p.is_dir()):
    ateliers = []
    for dossier_at in sorted(p for p in dossier_cours.iterdir() if p.is_dir()):
        fichiers = sorted(dossier_at.glob('*.md'))
        if not fichiers:
            continue
        notes, titre_at = [], ''
        for md in fichiers:
            meta, corps = lire(md)
            titre_at = phrase(meta.get('atelier_titre', dossier_at.name))
            chemin = md.relative_to(NOTES).as_posix()
            notes.append({'titre': meta.get('titre', md.stem), 'chemin': chemin})
            recherche.append({'c': chemin, 't': meta.get('titre', md.stem), 'a': titre_at, 'x': brut(corps)})
        numero = int(meta.get('atelier', 0))
        ateliers.append({'id': dossier_at.name, 'numero': numero, 'titre': titre_at, 'notes': notes})
    if ateliers:
        index.append({'id': dossier_cours.name, 'titre': COURS.get(dossier_cours.name, dossier_cours.name),
                      'ateliers': ateliers})

(NOTES / 'index.json').write_text(json.dumps({'cours': index}, ensure_ascii=False, indent=1), encoding='utf-8')
(NOTES / 'search.json').write_text(json.dumps(recherche, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
nb = sum(len(a['notes']) for c in index for a in c['ateliers'])
print(f'{len(index)} cours, {nb} notes -> notes/index.json, notes/search.json')

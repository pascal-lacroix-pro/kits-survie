#!/usr/bin/env python3
"""Convertit les GIF des notes en MP4 (beaucoup plus légers) et met à jour les .md.

Usage : python3 gif_vers_mp4.py DOSSIER_NOTES
- le GIF est remplacé par une balise <video> (lecture en boucle, avec contrôles)
- le GIF n'est supprimé que si le MP4 a bien été créé
"""
import re, sys, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

racine = Path(sys.argv[1])
gifs = sorted(racine.rglob('images/*.gif'))
VF = 'scale=trunc(iw/2)*2:trunc(ih/2)*2'


def convertir(gif):
    mp4 = gif.with_suffix('.mp4')
    r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(gif), '-movflags', 'faststart',
                        '-pix_fmt', 'yuv420p', '-vf', VF, '-an', str(mp4)], capture_output=True, text=True)
    ok = r.returncode == 0 and mp4.exists() and mp4.stat().st_size > 0
    return gif, mp4, ok, r.stderr.strip()[:200]


avant = sum(g.stat().st_size for g in gifs)
with ThreadPoolExecutor(max_workers=4) as ex:
    resultats = list(ex.map(convertir, gifs))

apres, echecs, ok_names = 0, [], set()
for gif, mp4, ok, err in resultats:
    if ok:
        apres += mp4.stat().st_size
        ok_names.add((gif.parent, gif.name))
        gif.unlink()
    else:
        echecs.append((gif, err))

balise = '<video src="images/{}.mp4" autoplay loop muted playsinline controls></video>'
modifs = 0
for md in racine.rglob('*.md'):
    texte = md.read_text(encoding='utf-8')
    def remplace(m):
        nom = m.group(1)
        return balise.format(nom) if (md.parent / 'images', nom + '.gif') in ok_names else m.group(0)
    nouveau, n = re.subn(r'!\[[^\]]*\]\(images/([^)]+?)\.gif\)', remplace, texte)
    if nouveau != texte:
        md.write_text(nouveau, encoding='utf-8')
        modifs += 1

print(f'GIF trouvés : {len(gifs)} | convertis : {len(ok_names)} | échecs : {len(echecs)}')
print(f'Poids : {avant/1e6:.0f} Mo -> {apres/1e6:.0f} Mo | notes modifiées : {modifs}')
for g, e in echecs:
    print('ECHEC', g, e)

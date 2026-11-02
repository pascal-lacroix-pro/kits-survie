# KITS SURVIE

Notes de cours en Markdown, consultables en lecture seule par les étudiant.e.s.

## Structure

```
notes/<cours>/<NN-atelier>/<NN-note>.md
notes/<cours>/<NN-atelier>/images/   ← images, vidéos et pièces jointes
outils/                              ← scripts de conversion
```

- Cours disponible : `apps-statiques` (59 notes, ateliers 1 à 25 + mémentos)
- Un fichier `.md` par note, préfixé par son ordre dans l'atelier
- `index.html` : page de lecture (à venir)

## En-tête d'une note

```
---
titre: 2-02. Créer un premier fichier HTML et le tester
cours: apps-statiques
atelier: 2
atelier_titre: "CRÉER & TESTER UN DOCUMENT HTML VALIDE"
ordre: 2
---
```

Les valeurs contenant `:` ou `&` sont mises entre guillemets.

## Fichiers non versionnés

Les `.zip` et les `.pdf` sont exclus du dépôt (`.gitignore`) pour garder un
dépôt léger. Ils restent dans les dossiers `images/` sur Dropbox.
⚠️ 9 notes contiennent des liens vers ces fichiers (22 liens au total) : ils sont
cassés en ligne tant qu'ils ne pointent pas vers Moodle ou Dropbox.

Les animations sont en `.mp4` (balise `<video>`), pas en GIF.

## Outils

- `outils/convert_nimbus.py` : export Nimbus Note (HTML) -> Markdown. Conversion
  faite une fois ; les `.md` sont désormais la source de vérité, ne pas relancer
  sans précaution (les corrections manuelles seraient écrasées).
- `outils/gif_vers_mp4.py` : GIF -> MP4 (nécessite `ffmpeg`).

## Ajouter ou modifier une note

1. Créer ou éditer le fichier dans `notes/<cours>/<atelier>/`
2. Reprendre l'en-tête ci-dessus
3. Rédiger en Markdown
4. Versionner : `git add . && git commit -m "Ajout note X" && git push`

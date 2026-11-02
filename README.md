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
- `index.html` + `assets/` : page de lecture en lecture seule (sans framework ; `marked` et `highlight.js` sont copiés dans `assets/vendor/`, aucun service externe)
- `notes/index.json` et `notes/search.json` : sommaire et recherche, **générés** par `outils/build_index.py` (non versionnés)

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

## Médias

Images, vidéos, PDF et zip sont versionnés dans les dossiers `images/` des ateliers.
Les animations sont en `.mp4` (balise `<video>`), pas en GIF.

## Outils

- `outils/convert_nimbus.py` : export Nimbus Note (HTML) -> Markdown. Conversion
  faite une fois ; les `.md` sont désormais la source de vérité, ne pas relancer
  sans précaution (les corrections manuelles seraient écrasées).
- `outils/gif_vers_mp4.py` : GIF -> MP4 (nécessite `ffmpeg`).

## Ajouter ou modifier une note (avec Obsidian)

Le coffre Obsidian est la racine du dépôt. Réglages (dans `.obsidian/`, non versionné) :
liens Markdown relatifs, pièces jointes dans `./images`, modèles dans `notes/_modeles`.

1. Obsidian → « Ouvrir un dossier comme coffre » → choisir `KITS_SURVIE/`
2. Nouvelle note : la créer dans le dossier de l'atelier, préfixée par son ordre
   (`03-ma-note.md`), puis insérer le modèle *Nouvelle note* (palette ⌘P → « Modèles »)
   et compléter l'en-tête
3. Rédiger ; coller ou glisser les images directement
4. Publier : plugin *Git* (⌘P → « Git: Commit-and-sync »)
   ou `git add . && git commit -m "Note X" && git push`

À chaque push, l'Action GitHub `.github/workflows/pages.yml` regénère le sommaire
et la recherche puis publie le site (≈ 1 min) :
https://pascal-lacroix-pro.github.io/kits-survie/

Tester en local (facultatif) : `python3 outils/build_index.py` puis
`python3 -m http.server 8000` et ouvrir http://127.0.0.1:8000
(ouvrir `index.html` directement ne fonctionne pas : le navigateur bloque la lecture des notes).

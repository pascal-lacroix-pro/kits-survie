---
titre: "3-02. Balises de structuration d'un document HTML"
cours: apps-statiques
atelier: 3
atelier_titre: CRÉER UN CODE HTML SÉMANTIQUE
ordre: 2
---

# 3-02. Balises de structuration d'un document HTML

## **1. Balises de structuration d'un document HTML**

Pour aller plus loin: [Référence des éléments HTML - HTML (HyperText Markup Language) | MDN](https://developer.mozilla.org/fr/docs/Web/HTML/Element)

|  |  | Balises | Sémantique | Exemples |
|---|---|---|---|---|
| 1 |  | `<!DOCTYPE html>` | Déclaration du type de document |  |
| 2 |  | `<html lang=""></html>` | Balise racine du document | `<html lang="fr">` `<head>...</head>` `<body>` `...` `</body>``</html>` |
| 3 |  | `<head></head>` | Titres et méta données du document | `<head>` `<meta charset="utf-8" />` `<title>Titre du document</title>``</head>` |
| 4 |  | `<meta />` | Méta données | `<head>` `<meta charset="UTF-8">` `<meta name="description" content="...">` `<meta name="keywords" content="HTML, ...">` `<meta name="author" content="John Doe">` `<meta name="viewport" content="width=device-width, initial-scale=1.0">``</head>` |
| 5 |  | `<title></title>` | Titre du document | `<head>` `<meta charset="utf-8" />` `<title>Titre du document</title>` `<link rel="stylesheet" src="css/app.css" />``</head>` |
| 6 |  | `<link rel="" src="" />` | Lien vers une feuille de style externe | `<head>` `...` `<link rel="stylesheet" src="css/app.css" />``</head>` |
| 7 |  | `<style></style>` | Intégration de code CSS interne | `<head>` `...` `<style>` `/* Ici vient du code CSS */` `</style>``</head>` |
| 8 |  | `<body></body>` | Corps du document | `<body>` `<h1>Titre du document</h1>` `<p>Lorem ipsum...</p>``</body>` |
| 9 |  | `<script></script>` | Intégration d'un script JS interne ou externe | `<body>` `...` `<script src="js/app.js"></script>` `<script>` `/* Ici vient du code JS */` `</script>``</body>` |
|  |  | All:9 | All:9 | All:9 |

## 2. Exemple de structuration d'un document HTML

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Kit de survie HTML - Balises de structuration d'un document HTML</title>
    <meta name="description" content="Lorem ipsum ...">
    <meta name="keywords" content="HTML, balises, validation, ...">
    <meta name="author" content="Pascal Lacroix">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/app.css" />
    <style>
      /* Ici vient du code CSS */
    </style>
  </head>
  <body>
    <h1>Kit de survie HTML</h1>
    <h2>Balises de structuration du document</h2>
    ...

    <script src="assets/js/app.js"></script>
  </body>
</html>
```

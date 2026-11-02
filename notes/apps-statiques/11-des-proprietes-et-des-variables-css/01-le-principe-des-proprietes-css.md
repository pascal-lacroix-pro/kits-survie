---
titre: 11-01. Le principe des propriétés CSS
cours: apps-statiques
atelier: 11
atelier_titre: DES PROPRIÉTÉS ET DES VARIABLES CSS
ordre: 1
---

# 11-01. Le principe des propriétés CSS

## 1. Une spécification, un point virgule

Dans chaque règle de style, on sépare les spécifications par des points-virgule

```css
.mon-style {
   background: orange;
   color: #fff;
}
```

## 2. Des super-propriétés

Lorsqu'une propriété comporte plusieurs sous-propriétés comme le background, le padding, ..., toutes ces sous-propriétés peuvent être regroupées en une seule super-propriété

```css
.mon-style {
   background-color: orange;
   background-image: url('assets/images/fond.png');

   padding-left: 1em
   padding-right: 2em;
   padding-top: 3em;
   padding-bottom: 4em}

/* Peut s'écrire */

.mon-style {
   background: orange url('assets/images/fond.png');
   padding: 3em 2em 4em 1em;
}
```

## 3. Les couleurs

Les couleurs peuvent s'écrire de 3 manières

1. Nom de la couleur en anglais ([&lt;color> - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/Type_color) )`background: red;`
2. Code hexadécimal avec un # (Rouge - Vert - Bleu)`background: #FF0000 ;` `background: #F00 ;`
3. Composante RVB avec transparence`background: rgba(255, 0, 0, .5);`

## 4. Les unités des mesure

- 1em est la taille de la police par défaut pour l'élément parent
- 1rem est la taille de la police par défaut pour l'élément racine (souvent 16px)
- px: nombre de pixels
- %: pourcentage de l'espace disponible de l'élément parent
- vh: pourcentage de la hauteur de la fenêtre du navigateur
- vw: pourcentage de la largeur de la fenêtre du navigateur

## 5. Traiter les dimensions avec la fonction calc()

La fonction calc() permet de calculer une dimension sur base d'unité différentes par exemple

```css
.ma-boite {
  width: calc(100% - 6em);
}
```

---

## RÉFÉRENCES

- [&lt;color> - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/color_value)
- [Valeurs et unités CSS - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Values_and_Units)
- [calc - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/calc())
- [Les variables CSS - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/Using_CSS_custom_properties)

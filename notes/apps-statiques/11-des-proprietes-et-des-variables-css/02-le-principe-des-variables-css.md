---
titre: 11-02. Le principe des variables CSS
cours: apps-statiques
atelier: 11
atelier_titre: DES PROPRIÉTÉS ET DES VARIABLES CSS
ordre: 2
---

# 11-02. Le principe des variables CSS

## 1. Les variables CSS

Il est possible en CSS de créer et d'utiliser des variables. C'est très pratique pour centraliser des valeurs communes à plusieurs déclarations CSS comme les couleurs de la palette, les polices, les tailles, ...

### Le scope ou portée des variables

Pour définir une variable, il faut lui attribuer une portée (un scope). La variable sera donc uniquement utilisable dans ce scope.

```css
/* Définition de variable au niveau racine: Accessible dans tout le document */
:root {
  --couleur1: orange;
  --couleur2: cyan;
  --font1:    Times, serif;
  --font2:    Verdana, sans-serif;
}

body {
  background: var(--couleur1);
  font-family: var(--font1);
}
h1 {
  font-family: var(--font2);
}
```

```css
.section1 {
  --font: Times, serif;
}
.section2 {
  --font: Times, serif;
}

.section1, .section2 {
  font-family: var(--font);
}

/* La variable aura une valeur différente selon le contexte */
```

---

## RÉFÉRENCES

- [&lt;color> - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/color_value)
- [Valeurs et unités CSS - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Values_and_Units)
- [calc - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/calc())
- [Les variables CSS - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/Using_CSS_custom_properties)

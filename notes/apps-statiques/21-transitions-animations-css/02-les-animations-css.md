---
titre: 21-02. Les animations CSS
cours: apps-statiques
atelier: 21
atelier_titre: "TRANSITIONS & ANIMATIONS CSS"
ordre: 2
---

# 21-02. Les animations CSS

## Les keyframes : pour créer des animations en CSS3

Les keyframe sont des ensemble d'images clés. Une animation est créée par, au minimum, 2 images clés. Chaque image clé est définie par des propriétés de style et le navigateur va animer les variations de propriétés d'une image clé à une autre.

Une animation, c'est une transition passant par plusieurs états.

### **1. On va d'abord définir l'animation et lui donner un nom**

```css
@keyframes mon-animation {
   from { background: orange; }
   to   { background: red; }
}
```

```css
@-webkit-keyframes mon-animation {
  0%   { background: orange; }
  100% { background: red;}
}
```

### **2. On utilise cette animation**

```css
.ma-classe {
   animation: mon-animation 5s infinite ease;
  -webkit-animation: mon-animation 5s infinite ease;
}
```

## Une animation peut avoir plus de 2 images clés

```css
@keyframes mon-animation {
     0%   { background: red; }
     33%  { background: blue; }
     78%  { background: yellow; }
     100% { background: green; }
}
```

## Utilisation de l'animation

```css
.ma-classe {
   animation-name: mon-animation;                
   animation-duration : 5s;                         
   animation-iteration-count: 2 | infinite;       
   animation-timing-function: ease | ease-in | ease-out | ...
   animation-delay: 2s;
   animation-direction: normal | alternate | reverse | alternate-reverse;
}

.ma-classe {
   animation: mon-animation 5s infinite ease 2s alternate;
}
```

---

## JE TE METS AU DÉFI !

### Pour t'échauffer:

[Exercise v3.0](https://www.w3schools.com/css/exercise.asp?filename=exercise_css3_animations1)

---

### Défi 1

<video src="images/iKRx2vanrWlSQ54d.mp4" autoplay loop muted playsinline controls></video>

Solution: [https://codepen.io/RYJASM/details/epdRZO](https://codepen.io/RYJASM/details/epdRZO)

---

---

## RÉFÉRENCES - Pour aller plus loin :

- [Utiliser les animations CSS - CSS : Feuilles de style en cascade | MDN](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Animations/Using_CSS_animations)
- [CSS Animations](http://www.w3schools.com/css/css3_animations.asp)
- [animation | CSS-Tricks](https://css-tricks.com/almanac/properties/a/animation/)
- [15 animations CSS vraiment bluffantes !](https://www.web-eau.net/blog/15-animations-css-vraiment-bluffantes)

---

## Librairies JS et CSS pour les animations

- [Animate.css | A cross-browser library of CSS animations.](https://animate.style/)
- [https://animista.net/play/basic/flip](https://animista.net/play/basic/flip)

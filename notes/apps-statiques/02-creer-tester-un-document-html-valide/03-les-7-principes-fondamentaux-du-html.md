---
titre: 2-03. Les 7 principes fondamentaux du HTML
cours: apps-statiques
atelier: 2
atelier_titre: "CRÉER & TESTER UN DOCUMENT HTML VALIDE"
ordre: 3
---

# 2-03. Les 7 principes fondamentaux du HTML

▶️ [Vidéo](https://www.youtube.com/watch?v=_QmhHd3ZVMk)

---

## HTML: Hypertext Markup Langage

On utilise des balises pour définir les objets à intégrer dans la page web (paragraphes, titres, liens, formulaires, ...). Pour que le document soit bien formé, ces balises doivent obéir aux principes suivants:

## 1. Deux types de balises

**Balises standard (avec contenu):** Une partie ouvrante (ici commence...) et une partie fermante (ici finit...).

```html
<h1>Ceci est le titre de la page</h1>
<p>Ceci est un paragraphe</p>
```

**Balises "objets" ou "orphelines", sans contenu:** On ferme la balise dans la partie ouvrante si on veut faire du XHTML (HTML respectant strictement la syntaxe XML)

```html
<!-- Version XHTML -->
<hr/>
<br/>
<img />

<!-- Version HTML -->
<hr>
<br>
<img>
```

## 2. 1000 espaces = 1 espace

```html
<h1>Ceci      est 
   mon                titre
</h1>

<!-- Est équivalent à -->

<h1>Ceci est mon titre</h1>
```

Donc, autant organiser son code de manière lisible

```html
<!-- Ceci est peu lisible -->
<h1>Ceci      est le 
  
 
 titre de la page</h1><p>Ceci      est un 
  
paragraphe</p>

<!-- Ceci est mieux ! :-) -->
<h1>Ceci est le titre de la page</h1>
<p>Ceci est un paragraphe</p>
```

## 3. Des balises de type bloc et des balises de type inline

**Balises de type bloc:** Le navigateur passe à la ligne avant ces balises

```html
<h1>Ceci est le titre de la page</h1>
<p>Ceci est un paragraphe</p>
```

**Balises de type inline:** pas de passage à la ligne

```html
<p>Ceci est un concept <strong>important</strong></p>
<p>Ceci est un concept <em>mis en évidence</em></p>
<p>Ceci est un <a>lien</a></p>
```

## 4. Pas de croisement de balises : le principe d'inclusion des balises

```html
<p>Un concept <strong>important</strong></p> <!-- OK -->
<p>Un concept <strong>important</p></strong> <!-- PAS OK -->
```

## 5. Toute balise peut contenir des attributs, séparés par des espaces, et placés uniquement dans la partie ouvrante

- Un attribut donne une information complémentaire au navigateur
- L'attribut se place dans la partie ouvrante de la balise
- Sa valeur est toujours entre guillemets
- On sépare les attributs par un espace

```html
<p title="Ceci est une infobulle" id="para1">Ceci est un paragraphe</p>
```

## 6. Les liens hypertexte

```html
<a href="http://www.promotion-sociale.be">Ceci est mon lien</a>
```

## 7. Les commentaires HTML

```html
<!-- Ceci est un commentaire HTML en une seule ligne -->

<!-- 
	Ceci est un commentaire HTML
	sur plusieurs lignes
-->

<!-- Ceci n'est PAS VALIDE ----------------------------------- -->
<!-- Ceci est VALIDE ######################################### -->
```

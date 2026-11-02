---
titre: 3-01. La sémantique des balises HTML
cours: apps-statiques
atelier: 3
atelier_titre: CRÉER UN CODE HTML SÉMANTIQUE
ordre: 1
---

# 3-01. La sémantique des balises HTML

## 1. La sémantique, c'est le sens d'une chose. Ce qu'elle signifie

Les balises HTML indiquent au navigateur de quel type de contenu il s'agit. Notre rôle est d'utiliser la balise ayant le plus de sens possible pour décrire l'élément que nous souhaitons placer dans notre page.

Par exemple, pour ajouter un titre principal, nous utiliserons la balise `<h1>...</h1>` et pour un paragraphe, nous utiliserons la balise `<p>...</p>`

## 2. On n'utilise pas les balises pour obtenir un effet visuel mais pour décrire l'information qu'elles contiennent

Si j'utilise une balise `<h1>...</h1>`, cette balise sera interprétée par le navigateur en grand et en gras. Mais cette balise ne sert EN AUCUN CAS à mettre un texte en grand et en gras. Elle sert à placer un titre principal, tout comme la balise `<strong></strong>` ne sert pas à mettre un texte en gras mais à définir le contenu comme étant très important.

Si on souhaite modifier l'apparence naturelle du contenu d'une balise, on se servira des CSS, c'est leur rôle !!!

## 3. Google n'aime pas les balises qui mentent !

Le moteur Google se sert de notre code pour comprendre où sont les éléments importants et les éléments moins importants. C'est notre code qui va permettre à Google de hiérarchiser l'information.

Si nous mentons sur le contenu d'une balise, juste pour obtenir un effet visuel par exemple, tout est foutu, notre hiérarchie est par terre !

---
titre: 22-01. Le design responsive
cours: apps-statiques
atelier: 22
atelier_titre: LE RESPONSIVE DESIGN
ordre: 1
---

# 22-01. Le design responsive

Il fut un temps où les sites web étaient accessibles uniquement via des navigateurs clients installés sur des ordinateur de bureau, voire des portables mais dont la dimension d'écran était assez semblable.L'enjeu était alors principalement de rendre les interfaces web compatible avec les différents navigateurs. Ce qui, en soi, n'a jamais été gagné d'avance ...Aujourd'hui, à ces considérations s'ajoutent le fait que nos sites sont également accessibles au travers d'autres média dont les dimensions deviennent très variables.Alors la question se pose : doit-on offrir la même expérience aux utilisateurs, quelque soit le support ?

C'est un peu ce qui va se passer si on ne spécifie rien de particulier.Par défaut, le site va automatiquement s'adapter à la largeur disponible et sera donc tout petit sur un petit écran. Il faudra alors zoomer pour pouvoir lire si on est sur un smartphone.

Evidemment cette technique est assez frustrante car, sur de petit écrans, puisque le site est exactement le même sur tous les supports, on devra scroller beaucoup horizontalement et verticalement si on doit zoomer pour pouvoir lire le texte ... cela devient vite inconfortable et peu convivial.

Alors il y a 4 stratégies pour faire face à ce problème :

1 - La stratégie du Fluid Design2 - La stratégie des états quantiques du design (expression personnelles)3 - La stratégie des expériences utilisateurs spécifiques (jQuery Mobile)4 - La stratégie de la séparation app/website

Et ces stratégies ne sont nullement exclusives. On peut faire un mix de ces stratégies. mais encore faut-il en connaitre les principes.

## Amélioration progressive VS dégradation élégante

Attention, il faut toujours rester attentif à rester dans une logique d'amélioration progressive et non dans celle d'une dégradation élégante qui a marqué de son empreinte frustrante et peu tolérante le design graphique des sites web du début des années 2000.

## La logique Mobile First

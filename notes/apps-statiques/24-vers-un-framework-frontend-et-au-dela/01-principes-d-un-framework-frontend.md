---
titre: "24-01. Principes d'un framework FrontEnd"
cours: apps-statiques
atelier: 24
atelier_titre: VERS UN FRAMEWORK FRONTEND ET AU-DELÀ
ordre: 1
---

# 24-01. Principes d'un framework FrontEnd

## De l'intérêt des frameworks CSS

### Ré-utilisabilité

Il est aujourd'hui indiscutable que l'utilisation de frameworks CSS améliore considérablement l'efficacité de nos réalisations front. Personne n'aurait l'idée, à part ma grand-mère, de ré-écrire à chaque projet un système de grille responsive par exemple. Ce serait une perte de temps considérable. Elle avait le temps ma grand-mère.

### Maintenabilité

Les frameworks permettent aussi une meilleure meilleure maintenabilité de nos CSS dans le sens où le code CSS devient plus facile à organiser. Il y a d'une part le framework et d'autre part la surcharge qui reprend les éléments non ré-utilisables de notre application.

Alors, évidemment, la surcharge peut-être bordélique. Mais là aussi il y a des outils qui vont nous permettre de nous organiser comme

- La nomenclature BEM: [Block-Element-Modifier (BEM) & CSS atomique -](https://blog.arcoptimizer.com/block-element-modifier-bem-css-atomique)
- La logique OOCSS: séparer les classes pour ne pas de répéter (DRY - Don't Repeat Yourself)
- La logique atomique qui se base sur les 2 concepts précédents
- La logique utilitaire à la Tailwind...

Les 3 premiers principes (voir ateliers suivants) sont très proches et se basent sur les mêmes concepts. L'idée est de respecter au mieux la logique DRY. En faire le moins possible quoi.

Plus la logique d'organisation et de nomenclature de vos classes est claire et plus votre code sera maintenable, c'est-à-dire qu'il sera lisible et manipulable pour vous et pour les autres.

## Des frameworks frontend

Certains frameworks comme Materialize, Bootstrap ou Foundation proposent, en plus des classes pour nos mises en page, des classes qui permettent d'intégrer des composants interactifs comme des navbars responsive, des slider, des modal box, des notifications et autres menus dropdown...

Ce qui signifie que ces framework ne cachent pas uniquement du code CSS mais également du JS. Ces éléments interactifs sont directement intégrés dans le framework et sont paramétrables via des variables.

Il suffit de mettre les étiquettes et le code du composant dans notre document HTML et le tour est joué ! Cool !

<video src="images/IaXhDz2BB9iBJ4Hj.mp4" autoplay loop muted playsinline controls></video>

<video src="images/4sJqOD8Bn9Hymi3k.mp4" autoplay loop muted playsinline controls></video>

---

## RÉFÉRENCES:

- [Bootstrap, Materialize, and Tailwind CSS: Which is best? - LogRocket Blog](https://blog.logrocket.com/bootstrap-materialize-tailwind-css-which-is-best/)
- [Le Design Atomique – 24 jours de web](https://www.24joursdeweb.fr/2013/le-design-atomique/)

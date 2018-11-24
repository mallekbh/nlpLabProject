But du mini projet
------------------
A travers ce mini-projet vous pourrez apprécier de façon pratique la puissance des techniques de
Traitement Automatique du Langage Naturel. Le problème qui vous est proposé ici vous permettra de
développer une application qui aidera les linguistes et lexicographes de la langue arabe à construire un
dictionnaire historique de la langue, c’est-à-dire un dictionnaire qui permet de suivre les
développements des différents sens et nuances des mots.

Travail demandé
---------------
Pour son fonctionnement, votre système devra faire ce qui suit

1 - Téléchargement du corpus de textes historiques et son organisation par périodes historiques

Vous vous chargerez d’écrire le code nécessaire pour télécharger le maximum de textes que vous
nettoierez et organiserez (automatiquement) si nécessaires, et par genres (Histoire, Religion,
Littérature, etc.) à l’intérieur d’une même période historique, etc. Vous ferez votre propre recherche et
téléchargerez tout ce que vous voudrez (à l’aide d’un programme Python que vous définirez et qui fera
partie de votre mini-projet).
Les fichiers du corpus devront être de type.xml avec des balises spécifiques que vous définirez pour
les besoins de votre application.

2 - Conception et Développement de la plateforme comme indiqué plus haut

* Réfléchissez à l’option de recherche en ligne si nécessaire, en plus du mode Offline, qui
devrait être disponible par défaut sur le corpus que vous aurez téléchargé.
* L’application devra permettre une utilisation
    ** En mode manuel : au lexicographe de l’utiliser pour définir lui/elle-même de nouvelles
       entrées du dictionnaire historique, auquel cas les entrées définies seront sauvegardées
       comme finalisées.
    ** En mode automatique : des mots seront pris de façon automatique à artir d’une ressource
       lexicale (dictionnaire classique) et seront définies comme nouvelles entrées dans le
       dictionnaire historique de façon automatique en suivant les sens/utilisations du mot
       historiquement (comme expliqué dans le point (2) de la section « Motivation ».) Ce qui
       sera défini ainsi sera sauvegardé mais avec une balise qui indiquera que ce n’est pas
       encore validé. Une telle entrée qui sera affiché sur votre interface, devra faire apparaitre
       cette information pour que le lexicographe puisse la valider (peut-être après corrections)
       ou la supprimer (auquel cas elle pourrait être sauvegardée dans un fichier/répertoire à
       part, au cas où on voudrait y revenir).
    
3 - Affichage des résultats
Votre application devra permettre de construire un dictionnaire historique de l’Arabe de façon
graduelle. Ceci veut dire que tout ce que vous définirez (une fois que votre système sera finalisé)
devra être sauvegardé, et mis à jour au fur et à mesure de l’utilisation de votre application en
prenant en considération ce qui a été expliqué plus haut.

# Projet PACE

## Choses à faire / Pour faire les choses bien

- ``Data.md`` tout ça
- Git
  * Faire un git distant (avec la v.1.0 du site fonctionnelle)
  * Faire des commits bien et tout ; avec le remote
  * VSCode remote-ssh-server (regarder l'extension)(ne pas oublier de Data.md)
  * Git Book ?
- Django
  * Suite un guide complet, la docs en ligne, whatever, mais voilà
- Visuel
  * Ajouter des animations
  * PACE Anime
- Faire les choses bien
  * Faire que Les font-sizes, la hauteur des divs, images, gifs, soient bien les mêmes sur toutes tailles d'écrans
  * ∃ des sites, logiciels, frameworks, IDEs, ..., pour faire ça ? Se renseigner
  * Elle doit pouvoir ajouter et supprimer les PACEs à volonté
  * Utiliser le JSON pour générer les boutons (aussi), et pour déployer tout le reste du site mdr
  * Faire des backups de la base de données
  * S'inspirer de **rezelator**
  * S'assurer que l'input ne peut pas buguer, en particulier avec des accents, caractères spéciaux...
  * S'assurer que quand ils font de l'input ils font pas de la merde
  * Capitaliser les noms de famille, prénoms : majuscule sir la 1ère lettre et après les tirets (attention il peut y avoir 2 tirets)
  * Boutons front page : 
    + avoir une banque de 20-50 paires de couleurs qui vont bien ensemble
    + les paires de couleurs entre normal et when-hovering (avec la souris) sont décoréllées pour permettre un truc un peu infini (sans redondance, enfin quasiment)
    + Faire qu'il y ait le bon nombre de boutons sur la front page selon l'année à laquelle on est - et selon si la coordinatrice en chef a rendu visible les PACE de l'année (scolaire) en cours
    + Les années scolaires devraient se finir les 31 juillet (ou 31 aout ?) et tout devrait se reset le 1 aout (ou le 1 septembre ?)
    + Pour les CSS, faire en sorte que le fichier CSS soit pas dégueu, il doit ficément y avoir possibilité de bien faire les choses (en particulier pas faire 30 fichiers ou quoi mais juste avoir un template de css et après mettre en "argument" les couleurs pour reproduire la même chose)
    Par exemple : dans le html, avoir une variable qui compte le nombre de boutons et qui met le bon nombre de boutons / ce serait peut-être plutpot du JS, enfin bref se renseigner, c'est spur qu'il y a moyen de faire des bails 
- Trucs de webdev
  * Préciser une taille de font : quelle est la meilleure manière ? cf. requête GPT : %, em, in, px, ......
  * Préviser les positions et les tailles : idem
  * Importer plusieurs fonts... Clean up le code (et tout)
- Déploiement futur
  * Interface pour qu'ils puissent upload eux-même
  * Scripts pour convertir les 1ères pages en images (HD, faire ça bien avec un truc propre), ajouter au JSON le truc qui va bien
  * Ajouter une barre de recherche stylée
  * Tester différents browsers (différentes versions ?)
  * 
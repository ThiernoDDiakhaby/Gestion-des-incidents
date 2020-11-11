# Gestion-des-incidents


    

Rapport du projet du module outils libres de programmation

Membre: 
Moussa Deme 
Momar Rocky Gueye
Thierno Demba Diakhaby
Oumar Niang

Table des matières
Introduction 
 Objectifs
     3) Analyse et Conception
3.1) Modélisation
3.2) Technologies utilisées
     4) Réalisation
     5) Conclusion










 Introduction

Dans le cadre de notre module Outils libre de développement Logiciel on a eu à développer un projet pour la validation de ce module pour mettre en pratique les compétences acquises durant celui-ci.

L’enjeux de ce projet était d'acquérir des compétences indispensables en entreprise comme le développement d’application en utilisant des outils que nous allons voir par la suite.  

 Objectifs

Le travail qui nous est demandé est de développer une application de notre choix avec Django ou Flask. C’est dans ce contexte que nous avons décidé de créer une application web nommée “Gestion des incidents” avec Flask. 
La principale fonctionnalité de cette application étant de gérer les problèmes techniques au sein de l'équipe de développement. Chaque membre de l'équipe pourra signaler des problèmes au niveau de la plateforme. Ainsi le chef de projet aura une visibilité beaucoup  plus claire de l'état d’avancement de chaque membre de l'équipe.
L’application dispose d’une première page de connexion ou d’inscription et une deuxième ou il a la possibilité d’ajouter sont incident. Pour les administrateurs cette page dispose des boutons modifier et supprimer pour changer un ou plusieurs incidents.

 3)      Analyse et Conception

Dans cette partie , nous allons en premier lieu faire une analyse succincte des besoins en vue de sortir les différentes fonctionnalités de notre plateforme. Ensuite nous allons définir une architecture du système, qui nous permettra, plus tard, d’implémenter la solution.
L’activité d’analyse et de conception permet de traduire les besoins fonctionnels et les contraintes issues du cahier des charges et de la spécification des exigences dans un langage plus professionnel et compréhensible par tous les individus intervenants dans la réalisation et l’utilisation de l’application.
3.1 ) Modélisation

Modèle Merise
Nous allons à travers notre modèle Merise de la figure ci-dessous, définir la manière dont les données seront stockées.
Le système possède deux types d’utilisateurs :
L’administrateur
 Le développeur 
Le système les différencie par leur rôle.










Spécifications textuelles des besoins:

Après une analyse de notre projet, notre application comprendra ainsi plusieurs acteurs que sont :
• L’administrateur : il doit d’abord s'authentifier. Il est responsable de la gestion des problèmes  que rencontrent les membres de l'équipe projet.
Ainsi il peut consulter,modifier et supprimer un problème.

• Le développeur: il doit d’abord s'authentifier. Il peut signaler le ou les problèmes qu’il rencontre au niveau du projet.
Il peut aussi consulter la liste des problèmes existants.

Diagramme des cas d’utilisation :

 Ce diagramme est destiné à représenter les besoins des utilisateurs par rapport au système.






Etude de l’architecture du système 

L’idée est de concevoir une architecture qui résume la structure globale de notre système.

La figure ci-dessus nous offre une vue générale de comment notre système se présente.

 3.2)  Technologies utilisées

Pour la réalisation d’un tel projet nous avons opté pour les technologies suivante:




Flask:

Flask est un micro framework open-source de développement web en Python. Il est classé comme microframework car il est très léger. Flask a pour objectif de garder un noyau simple mais extensible. Il n'intègre pas de système d'authentification, pas de couche d'abstraction de base de données, ni d'outil de validation de formulaires. Cependant, de nombreuses extensions permettent d'ajouter facilement des fonctionnalités.Il est distribué sous licence BSD.


Mysql:

MySQL Database Service est un service de base de données entièrement géré permettant de déployer des applications cloud natives à l'aide de la base de données open source la plus populaire au monde. Il est 100% développé, géré et pris en charge par l'équipe MySQL.


Git:

Git est un système de contrôle de version distribué pour suivre les modifications du code source pendant le développement de logiciels . Il est conçu pour coordonner le travail entre les programmeurs, mais il peut être utilisé pour suivre les changements dans n'importe quel ensemble de fichiers . Ses objectifs incluent la vitesse, l'intégrité des données et la prise en charge des flux de travail distribués et non linéaires.

Architecture technique 
Cette étape consiste à proposer une architecture technique qui consiste à faire les choix de technologies et d’organisation de composants logiciels les plus adaptés aux besoins et aux contraintes du projet.
Au niveau de la figure ci-dessous, nous avons l’architecture formée des technologies choisies.



4) Réalisation

Page d'accueil

Tout utilisateur qui veut accéder à l’application doit au préalable s’authentifier. La figure ci-dessous nous montre l’interface d’authentification des utilisateurs.
Si on a pas de compte on peut créer un compte en donnant son nom,prénom,email et mot de passe.





Utilisateur simple (exemple:Développeur)
Si c’est un utilisateur simple(Développeur), il est alors redirigé vers la page d’accueil à partir de laquelle il a une vue de l’ensemble de l’application.


















Signaler un problème


Ajout réussi


Administrateur
Si c’est un administrateur, il est redirigé vers l’espace d’administration où il pourra gérer les incidents du système:
Consulter le problèmes
modifier un problème
supprimer un problème
Signaler un problème


Authentification de l’administration





Consulter les problèmes



Modification



Modification réussi







Suppression



Suppression réussi




Outils de gestion de version

GITHUB:
Voici le lien github où  se trouve le repository commun à tous les membres  du projet:

https://github.com/ThiernoDDiakhaby/Gestion-des-incidents


5) CONCLUSION
Dans le cadre de notre cours “Outils libre de développement logiciel”, nous sommes chargés de réaliser un projet. Notre travail se base sur le développement d'une application sur les technologies vues en classe. Ceci nous amène à découvrir une nouvelle plateforme de développement et à enrichir notre savoir et notre expérience.

L'application permet à une équipe de développement informatique de gérer les problèmes que rencontre chaque membre de l'équipe durant le projet.  
Chaque utilisateur(administrateur,développeur) doit au préalable s'authentifier et ainsi il lui est permis d'accéder aux différentes fonctionnalités de l'application. En outre, la sauvegarde de ses paramètres d'accès, le transfert des données vers le serveur lors d'une quelconque activité. 

Durant le développement de ce projet nous avons utilisé les outils cités ci-dessous:
	
Flask qui est un framework python pour le développement web.
Mysql comme moteur de base de données.
Git comme outils de gestion de versionning de notre projet.



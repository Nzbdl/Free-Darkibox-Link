# Free-Darkiworld-Link

## Récupérateur de Lien Vidéo Darkibox

Ce projet permet de récupérer des liens vidéo à partir de l'API de Darkiworld en utilisant un identifiant vidéo. Le script enregistre la réponse JSON dans un fichier et extrait le lien vidéo dans un autre fichier texte.

## Prérequis

Avant d'exécuter le fichier `.exe`, assurez-vous d'avoir :

- Un compte valide sur Darkiworld.
- Les informations d'identification nécessaires (adresse e-mail et mot de passe).

## Dépendances

### Exécution du Fichier Exécutable

Le fichier `recuperer_url_darkibox.exe` a été créé de manière à ce que vous puissiez l'exécuter directement sans avoir besoin d'installer Python ou d'autres dépendances sur votre machine. Cela signifie que vous pouvez simplement télécharger le fichier `.exe` et l'exécuter sans configuration supplémentaire.

1. **Téléchargez le Fichier Exécutable** :
   - Assurez-vous d'avoir le fichier `recuperer_url_darkibox.exe` sur votre ordinateur.

2. **Double-cliquez sur le Fichier** :
   - Localisez le fichier `recuperer_url_darkibox.exe` dans l'explorateur de fichiers.
   - Double-cliquez sur le fichier pour l'exécuter.

3. **Interface Graphique** :
   - Une fenêtre s'ouvrira avec des champs pour entrer votre adresse e-mail, votre mot de passe, l'identifiant de la vidéo, votre session et votre token.
   - Suivez les instructions à l'écran pour vous connecter et récupérer le lien vidéo.

## Modifications Apportées au Script

- **Connexion avec GET** : Le script a été modifié pour utiliser une requête GET pour se connecter à Darkiworld, en envoyant les informations d'identification (email et mot de passe) dans l'URL.
- **Gestion des Cookies** : Le script récupère les cookies nécessaires après la connexion pour les utiliser lors de la récupération des liens vidéo.
- **Enregistrement des Erreurs** : Les erreurs de connexion et de récupération de lien sont enregistrées dans un fichier `error_log.txt` pour faciliter le débogage.
- **Interface Utilisateur** : Une interface graphique a été créée à l'aide de Tkinter pour rendre l'application plus conviviale.

## Avertissement Légal

L'utilisation de ce script pour récupérer des informations à partir de l'API de Darkiworld est à vos propres risques. L'auteur de ce projet ne peut être tenu responsable des conséquences de l'utilisation de ce script, y compris, mais sans s'y limiter, les violations des conditions d'utilisation de Darkiworld ou d'autres lois applicables.

### Clause de Non-Responsabilité

1. **Responsabilité de l'Utilisateur** : En utilisant ce script, vous reconnaissez que vous le faites à vos propres risques. L'auteur ne garantit pas que l'utilisation de ce script est légale ou conforme aux conditions d'utilisation de Darkibox ou d'autres services.

2. **Données Scrappées** : Ce script peut récupérer des données qui sont protégées par des droits d'auteur ou d'autres lois. L'utilisation de ces données sans autorisation peut constituer une violation des droits d'auteur. L'auteur ne peut être tenu responsable de l'utilisation illégale des données récupérées.

3. **Site Illégal** : Ce script interagit principalement avec DarkiWorld, qui génère des comptes premium non légaux pour accéder à des liens de vidéos hébergés sur Darkibox. Si DarkiWorld est considéré comme illégal, interagir avec celui-ci peut comporter des risques. L'auteur ne soutient pas l'utilisation de services illégaux et ne peut être tenu responsable des conséquences de l'utilisation de ce script.

4. **Aide à la Détection de Contenu Illégal** : Si vous trouvez du contenu illégal, il est recommandé de le signaler aux autorités compétentes plutôt que de scraper le site vous-même.

## Exemple de Cookies

Assurez-vous de remplacer les cookies dans le script par ceux de votre session Darkiworld. Vous pouvez les obtenir en utilisant les outils de développement de votre navigateur.

## Aide

Si vous avez des questions ou des problèmes, n'hésitez pas à ouvrir une issue sur le dépôt GitHub ou à contacter l'auteur.

---

## Notes de Mise à Jour

- **Version 1.0** : Lancement initial du projet avec des fonctionnalités de récupération de lien vidéo.
- **Version 1.1** : Ajout de la gestion des erreurs et de l'enregistrement des logs d'erreur dans un fichier texte.
- **Version 1.2** : Modification de la méthode de connexion pour utiliser une requête GET au lieu de POST, conformément aux exigences de l'API.

---

**Note** : Ce projet est uniquement à des fins éducatives. Assurez-vous de respecter les conditions d'utilisation de l'API Darkiworld.

Merci d'utiliser ce projet à des fins éducatives !

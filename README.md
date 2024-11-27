# Free-Darkibox-Link

# Récupérateur de Lien Vidéo Darkibox

Ce projet permet de récupérer des liens vidéo à partir de l'API de Darkibox en utilisant un identifiant vidéo. Le script enregistre la réponse JSON dans un fichier et extrait le lien vidéo dans un autre fichier texte.

## Dépendances

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances suivantes :

- **Python 3.x**
- **Bibliothèque `requests`**

### Installation des Dépendances

1. **Installer Python**

   #### Sur Windows

   - Téléchargez l'installateur de Python depuis le site officiel : [Python Downloads](https://www.python.org/downloads/windows/)
   - Exécutez l'installateur et assurez-vous de cocher l'option **"Add Python to PATH"**.
   - Suivez les instructions à l'écran pour terminer l'installation.

   #### Sur Linux

   - Ouvrez un terminal et exécutez la commande suivante pour installer Python :
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Installer la Bibliothèque `requests`**

   Une fois Python installé, vous pouvez installer la bibliothèque `requests` en utilisant `pip`. Exécutez la commande suivante dans votre terminal ou invite de commandes :
   ```bash
   pip install requests
   ```

## Utilisation

1. **Cloner le Dépôt**

   Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/Nzbdl/free-darkibox-link.git
   cd free-darkibox-link
   ```

2. **Exécuter le Script**

   Avant d'exécuter le script, assurez-vous de modifier les cookies dans le script pour qu'ils correspondent à votre session Darkibox.

   Exécutez le script avec l'identifiant vidéo souhaité :
   ```bash
   python recuperer_url_darkibox.py <video_id>
   ```

   Remplacez `<video_id>` par l'identifiant de la vidéo que vous souhaitez récupérer.

3. **Résultats**

   - Le fichier `response_data.json` contiendra la réponse JSON complète de l'API.
   - Le fichier `darkibox-link.txt` contiendra le lien vidéo ou un message indiquant qu'aucun lien n'a été trouvé.

## Exemple de Cookies

Assurez-vous de remplacer les cookies dans le script par ceux de votre session Darkibox. Vous pouvez les obtenir en utilisant les outils de développement de votre navigateur.

## Aide

Si vous avez des questions ou des problèmes, n'hésitez pas à ouvrir une issue sur le dépôt GitHub ou à contacter l'auteur.

---

**Note** : Ce projet est uniquement à des fins éducatives. Assurez-vous de respecter les conditions d'utilisation de l'API Darkibox.

# recuperer_url_darkibox.py
import requests
import argparse
import json

def get_video_link(video_id, cookies):
    # URL de l'API pour récupérer le lien vidéo
    api_url = f"https://darkiworld.xyz/api/v1/download/{video_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': 'application/json',
        'X-XSRF-TOKEN': cookies.get('XSRF-TOKEN', ''),  # Inclure le token XSRF
        'Referer': f'https://darkiworld.xyz/download/{video_id}',
    }
    
    # Effectuer la requête GET avec les cookies
    response = requests.get(api_url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        data = response.json()  # Convertir la réponse en JSON
        
        # Enregistrer la réponse JSON dans un fichier
        with open('response_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)  # Écrire la structure JSON formatée
        
        # Extraire le lien vidéo
        video_link = data.get('video', {}).get('lien', None)  # Accéder au lien vidéo
        
        # Enregistrer le lien vidéo dans un fichier texte
        with open('darkibox-link.txt', 'w', encoding='utf-8') as link_file:
            if video_link:
                link_file.write(f"Lien vidéo : {video_link}\n")
            else:
                link_file.write("Aucun lien vidéo trouvé.\n")
    else:
        print(f"Erreur de récupération, code de statut : {response.status_code}")

# Configuration de l'argument parser
parser = argparse.ArgumentParser(description='Récupérer le lien vidéo à partir d\'un identifiant.')
parser.add_argument('video_id', type=int, help='L\'identifiant de la vidéo')

# Analyser les arguments
args = parser.parse_args()

# Exemple de cookies (remplacez par vos cookies réels)
cookies = {
    'darkiworld_session': '',
    'XSRF-TOKEN': '',
    # Ajoutez d'autres cookies si nécessaire
}

# Récupérer le lien vidéo
get_video_link(args.video_id, cookies)
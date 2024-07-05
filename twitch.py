import requests
import os
from dotenv import load_dotenv

load_dotenv()
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')

twitch_token = None

def get_twitch_token():
    global twitch_token
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': TWITCH_CLIENT_ID,
        'client_secret': TWITCH_CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        twitch_token = response.json()['access_token']
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen des Twitch-Tokens: {e}")

def get_twitch_user_info(username):
    if not twitch_token:
        get_twitch_token()
    url = 'https://api.twitch.tv/helix/users'
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {twitch_token}'
    }
    params = {
        'login': username
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        if data:
            return data[0]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Twitch-Nutzerinformationen für {username}: {e}")
        return None

def is_user_online(username):
    if not twitch_token:
        get_twitch_token()
    url = 'https://api.twitch.tv/helix/streams'
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {twitch_token}'
    }
    params = {
        'user_login': username
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        return len(data) > 0 and data[0]['type'] == 'live'
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen des Twitch-Status für {username}: {e}")
        return False

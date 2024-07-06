import requests
import os
from dotenv import load_dotenv
from config import config
import requests

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
        print(f"Error while getting the token: {e}")

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
        print(f"Error while getting userinformation for: {username}: {e}")
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
        print(f"Error while getting online_status for: {username}: {e}")
        return False

def get_twitch_api_headers():
    # Hier sollten die notwendigen Header für die Twitch API-Aufrufe generiert werden
    # Dies könnte z.B. eine OAuth-Token-Authentifizierung beinhalten
    return {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {twitch_token}'
    }

def get_stream_info(username):
    headers = get_twitch_api_headers()
    user_info_response = requests.get(f"https://api.twitch.tv/helix/users?login={username}", headers=headers)
    user_info = user_info_response.json()

    if 'data' not in user_info or len(user_info['data']) == 0:
        return {'online': False}

    user_id = user_info['data'][0]['id']
    stream_info_response = requests.get(f"https://api.twitch.tv/helix/streams?user_id={user_id}", headers=headers)
    stream_info = stream_info_response.json()

    if stream_info['data']:
        stream = stream_info['data'][0]
        return {
            'online': True,
            'title': stream['title'],
            'game': stream['game_name'],
            'url': f"https://www.twitch.tv/{username}"
        }
    else:
        return {'online': False}

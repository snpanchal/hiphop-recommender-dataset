import requests
import os
from dotenv import load_dotenv


class Album:
    def __init__(self, id, name, explicit):
        self.id = id
        self.name = name
        self.explicit = explicit


def get_request_headers():
    load_dotenv('../.env')
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/api/token'

    spotify_auth_reponse = requests.post(SPOTIFY_AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET
    })

    auth_data = spotify_auth_reponse.json()
    access_token = auth_data['access_token']
    return {
        'Authorization': 'Bearer {}'.format(access_token)
    }


def remove_duplicates(albums_list):
    albums_map = {}
    for album in albums_list:
        if ((not album.name.lower() in albums_map) or (not albums_map[album.name].explicit)):
            albums_map[album.name.lower()] = album

    return list(albums_map.values())

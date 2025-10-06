import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv


import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)


artist_uri = 'spotify:artist:6XyY86QOPPrYVGvF9ch6wz'


results = spotify.artist_top_tracks(artist_uri)


for track in results['tracks'][:10]:
    print('🎵 Track    :', track['name'])
    print('🔗 Audio    :', track['preview_url'])
    print('🖼️ Cover art:', track['album']['images'][0]['url'])
    print()
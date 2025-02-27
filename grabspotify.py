import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read"
))

def get_liked_songs():
    songs = []
    # Only able to receive 50 songs at a time so my recommendation is load the first 50 songs
    # make a new temp file and continue to put each iteration of 50 songs in there
    # then load them all back in "spotify_liked_songs"
    results = sp.current_user_saved_tracks(limit=50, offset=0)
    for item in results['items']:
        track = item['track']
        songs.append(f"{track['name']} {track['artists'][0]['name']}")
    return songs

# Save liked songs to a file
with open("spotify_liked_songs.txt", "w") as file:
    for song in get_liked_songs():
        file.write(song + "\n")
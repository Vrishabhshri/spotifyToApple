import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "5c1bd783da1e494c9cfe29feecedd547"
SPOTIFY_CLIENT_SECRET = "141c886d25e7471085fccb3a3f96ad5d"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read"
))

def get_liked_songs():
    songs = []
    results = sp.current_user_saved_tracks(limit=50, offset=950) # change to 1000
    for item in results['items']:
        track = item['track']
        songs.append(f"{track['name']} {track['artists'][0]['name']}")
    return songs

# Save liked songs to a file
with open("spotify_liked_songs.txt", "w") as file:
    for song in get_liked_songs():
        file.write(song + "\n")
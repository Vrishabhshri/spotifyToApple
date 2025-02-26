I would like to preface with this:
This program is meant for users transferring from Spotify premium to Apple Music and does require you have Spotify premium
during the process.

This is a converter that grabs your songs from Spotify and adds them to Apple Music the slow (but free) way. 
It basically simulates going to the Apple Music web player and adding each song by search.

What you'll need to do:

In terminal of this directory:

1. pip install selenium
2. pip install spotipy

Create a .env file in this project directory and add the following variables that can be found
in the Spotify Developer Program that comes with every Premium account

SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=your_redirect_uri
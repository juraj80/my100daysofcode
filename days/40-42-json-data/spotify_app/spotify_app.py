import os
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser
from json.decoder import  JSONDecodeError

client_id = 'c5c5fe880ac24a6593550a9c147aaaa7'
client_secret = '17b6bca8787e40919f00438f2a4144b6'
# redirect_uri = 'http://google.com'

# Get the username from terminal
username = sys.argv[1]

# User ID: 11169195347

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret,
                                       redirect_uri='http://google.com')
except:
    # raise ValueError("Invalid token")
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret,
                                       redirect_uri='http://google.com')

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()
#print(json.dumps(user, sort_keys=True, indent=4))

while True:

    print()
    print(">>> Welcome to Spotipy")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print()
        searchQuery = input("Artist Name: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        print(json.dumps(user, sort_keys=True, indent=4))

        artist = searchResults["artists"]["items"][0]
        print(artist["name"])
        print(f'{str(artist["followers"]["total"])} followers.')
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])

        # Album and track details



    # End the program
    if choice == "1":
        break
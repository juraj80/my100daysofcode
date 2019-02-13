import os
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser

client_id = 'c5c5fe880ac24a6593550a9c147aaaa7'
client_secret = '3bc37e3c4ad14c08b1c24e5ab7f6e04a'
redirect_uri = 'http://google.com'

# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# User ID: 11169195347

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret,
                                       redirect_uri)
except:
 #   raise ValueError("Invalid token")
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username, scope, client_id, client_secret,
                                       redirect_uri)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

# Get current device
devices = spotifyObject.devices()
# print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

# Current track information
track = spotifyObject.current_user_playing_track()
# print(json.dumps(track, sort_keys=True, indent=4))
print()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist != "":
    print("Currently playing {} - {}".format(artist, track))


# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']
#print(json.dumps(user, sort_keys=True, indent=4))

while True:

    print()
    print(">>> Welcome to Spotipy {}".format(displayName))
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
        # print(json.dumps(user, sort_keys=True, indent=4))

        artist = searchResults["artists"]["items"][0]
        print(artist["name"])
        print(f'{str(artist["followers"]["total"])} followers.')
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print('ALBUM {}'.format(item['name']))
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print('{} :  {}'.format(str(z), item['name']))
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z += 1
            print()

        # See album art
        while True:
            songSelection = input("Enter a song number to see the album art and play the song (x to exit): ")
            if songSelection == 'x':
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID, None, trackSelectionList)
            webbrowser.open(trackArt[int(songSelection)])

    # End the program
    if choice == "1":
        break
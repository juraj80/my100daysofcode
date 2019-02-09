#!python3
import json
import requests
from pprint import pprint
user_id = 11169195347
# url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
#
client_id = 'c5c5fe880ac24a6593550a9c147aaaa7'
client_secret = '17b6bca8787e40919f00438f2a4144b6'

# import spotipy
# sp = spotipy.Spotify()
#
# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
#     print(' ', i, t['name'])

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print ("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username, scope)
token = util.prompt_for_user_token(username=user_id,scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost:8888?=https://accounts.spotify.com/authorize?client_id=c5c5fe880ac24a6593550a9c147aaaa7&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8888&scope=user-library-read')
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)

# r = requests.get(url)
#
# data = json.loads(r.text)
#
# for item in data.items():
#     print(item)
#
# #Hard to read
#
# for item in data.items():
#     pprint(item)
#
# #easier to read

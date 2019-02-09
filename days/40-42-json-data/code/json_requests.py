#!python3

import json
import requests
from pprint import pprint
user_id = 11169195347
url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

client_id = 'c5c5fe880ac24a6593550a9c147aaaa7'
client_secret = '17b6bca8787e40919f00438f2a4144b6'


r = requests.get(url)

data = json.loads(r.text)

for item in data.items():
    print(item)

#Hard to read

for item in data.items():
    pprint(item)

#easier to read

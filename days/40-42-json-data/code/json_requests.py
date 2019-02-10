#!python3

import json
import requests
from pprint import pprint

r = requests.get(url)

data = json.loads(r.text)  # returns an object from a string

for item in data.items():
    print(item)

#Hard to read

for item in data.items():
    pprint(item)

#easier to read

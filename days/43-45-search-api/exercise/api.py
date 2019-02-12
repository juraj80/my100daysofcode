from typing import List

import requests
from collections import namedtuple


Episode = namedtuple('Episode', 'category, id, url, title, description')


def get_results_from_api(keyword: str) -> List[Episode]:
    url = 'http://search.talkpython.fm/api/search?q={}'.format(keyword)
    resp = requests.get(url)

    resp.raise_for_status()
    result = resp.json()
    episodes = []

    for item in result['results']:
        if item['category'] == 'Episode':
            episodes.append(Episode(**item))

    return episodes


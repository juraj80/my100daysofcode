import requests


def get_results_from_api(keyword:str):
    url = 'http://search.talkpython.fm/api/search?q={}'.format(keyword)
    resp = requests.get(url)

    resp.raise_for_status()
    print(resp)
    return resp.json()



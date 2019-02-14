import requests

def get_results_from_api():
    url = 'https://dennikn.sk/api/minute'
    resp = requests.get(url)
    resp.raise_for_status()
    site_json = resp.json()
    results = []
    for item in site_json['timeline']:
        results.append(item['content']['main'])

    return results


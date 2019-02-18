import requests

URL = "https://store.steampowered.com/feeds/news.xml"

if __name__ == '__main__':
    resp = requests.get(URL)
    with open('newreleases.xml','wb') as f:
        f.write(resp.content)
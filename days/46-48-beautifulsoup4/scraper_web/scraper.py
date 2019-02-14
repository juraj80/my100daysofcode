import bs4
import requests

URL = 'https://dennikn.sk'

def pull_site():
    raw_site = requests.get(URL)
    raw_site.raise_for_status()
    return raw_site

def scrape_web(site):
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
#   print(soup.get_text())
#   print(soup.prettify())
    a_mpm_posted = soup.find_all('p')
    for item in a_mpm_posted:
       print(item.text)

if __name__ == '__main__':
    site = pull_site()
    print(scrape_web(site))
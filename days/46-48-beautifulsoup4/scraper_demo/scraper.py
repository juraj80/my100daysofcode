import requests
import bs4

# URL of site we want to scrape
URL = "https://pybit.es/pages/projects.html"

def pull_site(): # requests best practice - in production put this script in different file and here use just BS4
    raw_site_page = requests.get(URL) #Pull down the site.
    raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
    return raw_site_page

def scrape(site):
    header_list = []
    #Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')  # in this case the name of specific css class

    for headers in html_header_list:
        header_list.append(headers.getText())  # just plain string text from whole h3 tag
    for headers in header_list:
        print(headers)


if __name__ == "__main__":
    site = pull_site()
    scrape(site)

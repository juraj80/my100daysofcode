import api
from pprint import pprint

def main():

    keyword = input("What keyword to search for?  <ENTER WORDS>: ")

    results = api.get_results_from_api(keyword)
    print('There are {} matching results: '.format(len(results['results'])))

    for idx, item in enumerate(results['results'], 1):
        print('{}. {}'.format(idx, item['title']))

if __name__ == '__main__':
    main()
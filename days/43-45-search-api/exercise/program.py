import api
from pprint import pprint

def main():

    keyword = input("What keyword to search for?  <ENTER WORDS>: ")

    episodes = api.get_results_from_api(keyword)
    print('There are {} matching results: '.format(len(episodes)))

    for idx, item in enumerate(episodes, 1):
        print('{}. {}'.format(idx, item.title))

if __name__ == '__main__':
    main()
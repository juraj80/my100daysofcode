import api
from pprint import pprint


def main():

    keyword = input("What keyword to search for?  <ENTER WORDS>: ")

    episodes = api.get_results_from_api(keyword)
    print('There are {} matching results: '.format(len(episodes)))
    # episodes = sorted(episodes,key=lambda x: x.id)
    for item in sorted(episodes, key=lambda x: x.id):
        print('{}. {}'.format(item.id, item.title))
    print()

    episodesID = [item.id for item in episodes]

    number = int(input("Enter the episode number to show the episode page: "))

    if number not in episodesID:
        print("The number is not a valid episode number.")
    else:
        api.display_url_from_episode(number, episodes)

if __name__ == '__main__':
    main()


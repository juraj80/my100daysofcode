from api import MovieSearchClient

def main():
    msc = MovieSearchClient()
    resp = msc.search_movie('Capital')
    print(resp.json())

if __name__ == '__main__':
    main()
from api import MovieSearchClient
import collections

MovieResult = collections.namedtuple('MovieResult', 'imdb_code, title, director, keywords, '
                                     'duration, genres, rating, year, imdb_score')

def print_header():
    print('------------------------------------------')
    print('        MOVIE SEARCH SERVICE              ')
    print('------------------------------------------')
    print()

def search_event_loop():

    while True:
        print('Search movies by: ')
        print()
        print('      [1] movie title')
        print('      [2] director')
        print('      [3] imdb code')
        print()
        key = input('Enter your choice [number]: ')

        if key == '1':
            movie_string = input('Enter a movie name: ')
            movies = search_movies(movie_string)
            print()
            print("Found {} movies for '{}' search : ".format(len(movies.get('hits')), movie_string))
            print()
            print_movies(movies)

        elif key == '2':
            director_string = input('Enter a director name: ')
            movies = search_movies_by_director(director_string)
            print()
            print("Found {} movies for '{}' search : ".format(len(movies.get('hits')), director_string))
            print()
            print_movies(movies)

        elif key == '3':
            while True:
                try:
                    imdb_number = input('Enter imdb number of a movie: ')
                    movie = search_movies_by_imdb_code(imdb_number)
                except:
                    print()
                    print("Wrong imdb number! ")
                    print()
                
            r = MovieResult(**movie)
            print(f'Title: {r.title}')
            print(f'Director: {r.director}')
            print(f'Year: {r.year}')
            print(f'Imdb score: {r.imdb_score}')
            print()

        else:
            print('Wrong choice !')
            break

def search_movies(movie_title):
    msc = MovieSearchClient()
    resp = msc.get_movies(movie_title)
    results = resp.json()
    return results

def search_movies_by_director(director_name):
    msc = MovieSearchClient()
    resp = msc.get_movies_by_director(director_name)
    results = resp.json()
    return results

def search_movies_by_imdb_code(imdb_code):
    msc = MovieSearchClient()
    resp = msc.get_movies_by_imdb_code(imdb_code)
    result = resp.json()
    return result

def print_movies(movies_dict):
    movies = [MovieResult(**movie) for movie in movies_dict.get('hits')]

    movies.sort(key=lambda x: -x.year)

    for m in movies:
        print(f'Title: {m.title}')
        print(f'Director: {m.director}')
        print(f'Year: {m.year}')
        print(f'Imdb score: {m.imdb_score}')
        print()

def main():
    print_header()
    search_event_loop()

if __name__ == '__main__':
    main()
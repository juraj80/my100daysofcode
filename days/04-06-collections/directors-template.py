from collections import defaultdict, namedtuple, Counter
import csv
import random
from urllib.request import urlretrieve


movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'

movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    '''Extracts all movies from csv and stores them in a dictionary
        where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data) as f: # The Pythonic way to open a file is to use a context manager ('with' statement)
        for line in csv.DictReader(f): # to parse every line to OrderedDict
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0','')
                year = int(line['title_year'])
                score = float(line['imdb_score'])

            except ValueError: # a value error got raised for some rows, so when that happened, we just ignored the row
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m) # defaultdict in action, we don't have to initialize an empty list up front for every director

    return directors

#

def main():
    directors = get_movies_by_director()
    # lookup for Christopher Nolan
    print(directors['Christopher Nolan'])

    # get the 5 directors with the most movies.
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print(cnt.most_common(5))


if __name__ == '__main__':
    main()
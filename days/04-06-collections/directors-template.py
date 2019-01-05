from collections import defaultdict, namedtuple, Counter
import csv
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'

movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

# csv structure:
# color,director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,gross,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,movie_facebook_likes
# Color,James Cameron,723,178,0,855,Joel David Moore,1000,760505847,Action|Adventure|Fantasy|Sci-Fi,CCH Pounder,Avatar ,886204,4834,Wes Studi,0,avatar|future|marine|native|paraplegic,http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1,3054,English,USA,PG-13,237000000,2009,936,7.9,1.78,33000
# Color,Gore Verbinski,302,169,563,1000,Orlando Bloom,40000,309404152,Action|Adventure|Fantasy,Johnny Depp,Pirates of the Caribbean: At World's End ,471220,48350,Jack

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    '''Extracts all movies from csv and stores them in a dictionary
        where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data) as f: # The Pythonic way to open a file is to use a context manager ('with' statement)
        for line in csv.DictReader(f): # https://docs.python.org/3.4/library/csv.html - creates an object which operates like a regular reader csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds). If the fieldnames parameter is omitted, the values in the first row of csvfile will be used as the fieldnames
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

def main():
    directors = get_movies_by_director()

    print(directors)


    # lookup for Christopher Nolan
    print(directors['Christopher Nolan'])

    # get the 5 directors with the most movies.
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)
    print(cnt.most_common(5))

if __name__ == '__main__':
    main()
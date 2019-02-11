from typing import List
import json
import requests
import collections
from pprint import pprint


Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:  # type hint, it enables hints for method
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()
#    results = json.loads(resp.text)
    results = resp.json()  # requests method json() converts json into python dics
    pprint(results)
    movies = []
    for r in results.get('hits'):  # for dict in list of movies
        # movie = Movie(imdb_code = r['imdb_code'],
        #               title = r['title'],
        #               director = r['director'],
        #               keywords=r['keywords'],
        #               duration=str(r['duration']),
        #               genres=r['genres'],
        #               rating=r['rating'],
        #               year=str(r['year']),
        #               imdb_score=str(r['imdb_score'])
        #     )
        # movies.append(movie)
        movies.append(Movie(**r))

    return movies

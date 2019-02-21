import uplink
import requests


class MovieSearchClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')

    @uplink.get('/api/search/{keyword}')
    def get_movies(self, keyword) -> requests.models.Response:
        """ Get all movie entries from the server by keyword. """

    @uplink.get('/api/director/{director_name}')
    def get_movies_by_director(self, director_name) -> requests.models.Response:
        """ Get all movie entries from the server by director. """

    @uplink.get('/api/movie/{imdb_number}')
    def get_movies_by_imdb_code(self, imdb_number):
        """ Get movie from the server by imdb number. """




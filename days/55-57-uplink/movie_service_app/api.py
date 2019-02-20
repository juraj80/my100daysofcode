import uplink
import requests


class MovieSearchClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')

    @uplink.get('/api/search/{keyword}')
    def search_movie(self,keyword) -> requests.models.Response:
        """ Search movie entries from the server by keyword. """


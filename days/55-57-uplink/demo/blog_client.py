import datetime

import requests
import uplink

from uplink_helpers import raise_for_status


@uplink.json    # for uplink.body, we had to specify JSON otherwise it's going to pass it as form encoded to the server
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://consumer_services_api.talkpython.fm') # default argument for a BlogClient class

    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """ Get's all blog entries from the server. """

    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Get single blog post details. """

    def create_new_entry(self, title: str, content: str,            # for uplink.post we wrote this wrapper function that takes meaningful arguments, with default values
                         views: int = 0, published: str = None) -> requests.models.Response:
        if published is None:
            published = datetime.datetime.now().isoformat()

        # noinspection PyTypeChecker
        return self.__create_new_entry(    # and then return this hidden internal function that routes to our url/api/blog
            title=title,
            content=content,
            view_count=views,
            published=published
        )

    @uplink.post('/api/blog')
    def __create_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """ Creates a new post. """

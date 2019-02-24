from collections import namedtuple, Counter
import twitter_credentials
import os
import re

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tweepy
from wordcloud import WordCloud, STOPWORDS

Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'JurajKlucka'

# TWITTER_KEY = os.environ['TWITTER_KEY']
# TWITTER_SECRET = os.environ['TWITTER_SECRET']
# TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
# TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(twitter_credentials.TWITTER_KEY, twitter_credentials.TWITTER_SECRET)
auth.set_access_token(twitter_credentials.TWITTER_ACCESS_TOKEN, twitter_credentials.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)


tweets = list(get_tweets())

print(len(tweets))

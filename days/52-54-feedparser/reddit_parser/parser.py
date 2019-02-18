#! usr/bin/env python3
import praw

reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS',
                     client_secret='SECRET_KEY_27_CHARS ',
                     user_agent='YOUR_APP_NAME',
                     username='YOUR_REDDIT_USER_NAME',
                     password='YOUR_REDDIT_LOGIN_PASSWORD')


subreddit = reddit.subreddit('algotrading')

top_subreddit = subreddit.top(limit=50)

for submission in top_subreddit:
    print('Title: {}'.format(submission.title))
    print('Score: {}'.format(submission.score))
    print('Id: {}'.format(submission.id))
    print('Url: {}'.format(submission.url))
    print()
import feedparser

FEED_FILE = "newreleases.xml"

print(FEED_FILE)

# feed = feedparser.parse(FEED_FILE)
feed = feedparser.parse(r'newreleases.xml')
print('Feed Title: {}'.format(feed['feed']['title']))

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title} : {entry.link}')

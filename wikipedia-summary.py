import wikipedia
import re
import praw
from urllib.parse import urlparse
from config import credentials

# create reddit instance
info = credentials()
reddit = praw.Reddit(user_agent = "Wikipedia Summary Bot (by /u/KobeeKodes)", 
                     client_id = info[0], client_secret = info[1])

for comment in reddit.subreddit('all').stream.comments():
    if ('https://en.wikipedia.org/wiki' or 'http://en.wikipedia.org/wiki') in str(comment.body):
        #print(str(comment.body))
    
        urls = re.findall(r'http[s]?://en.wikipedia.org/wiki/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+[^]?]', comment.body)
        print(urls)
        # extract topic
        topics = []
        for url in urls:
            if 'https' in url:
                topics.append(url[30:])
            else:
                topics.append(url[29:])

        for topic in topics:
            topic = topic.replace('_', ' ').replace('%','').replace(r'%+[0-9]+', '').replace('\\', '').replace('\n', '').replace('(', '').replace(')', '')
            print(topic)
            try:
                default_summary = wikipedia.summary(topic)
                summary = default_summary.split('\n')[0]
                comment.reply(summary)
            except:
                print('Failed on query: ' + topic)
                continue
            print(summary)
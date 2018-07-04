import wikipedia
import re
import praw
from config import credentials

# create reddit instance
info = credentials()
reddit = praw.Reddit(user_agent = "Wikipedia Summary Bot (by /u/KobeeKodes)", 
                     client_id = info[0], client_secret = info[1])

# core logic once plain URL is obtained
if 'https://en.wikipedia.org/wiki/' in message:
    url = url.replace('https://en.wikipedia.org/wiki/', '')
    target_page = wikipedia.page(url.replace('_', ''))

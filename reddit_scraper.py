import os
import praw
from dotenv import load_dotenv

def fetch_reddit_snippets(subreddit, limit=5):
    load_dotenv('../config/api_keys.env')
    reddit = praw.Reddit(client_id=os.getenv('PRAW_CLIENT_ID'),
                         client_secret=os.getenv('PRAW_CLIENT_SECRET'),
                         user_agent='sirshaqbot')
    posts = reddit.subreddit(subreddit).top('day', limit=limit)
    return [p.title for p in posts]

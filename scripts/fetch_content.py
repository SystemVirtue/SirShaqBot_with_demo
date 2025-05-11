"""
Fetch and filter text snippets from Reddit, Twitter, etc., or load demo data.
"""
import os
from datetime import datetime
from utils.config import is_demo_mode

if is_demo_mode():
    from utils.media_collector import load_demo_text_snippets as fetch_snippets
else:
    from utils.reddit_scraper import fetch_reddit_snippets as fetch_snippets
    from utils.media_collector import download_cat_clips as fetch_media


def main():
    print(f"[{datetime.now()}] Starting content fetch...")
    snippets = fetch_snippets(subreddit='AskReddit', limit=10)
    if not is_demo_mode():
        fetch_media(count=5)
    else:
        print("DEMO mode: using sample media & text snippets.")

if __name__ == '__main__':
    main()

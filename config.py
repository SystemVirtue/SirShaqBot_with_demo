import os

def is_demo_mode():
    placeholders = {
        'PRAW_CLIENT_ID': 'your_id',
        'PRAW_CLIENT_SECRET': 'your_secret',
        'TWITTER_BEARER_TOKEN': 'your_token',
        'YOUTUBE_CLIENT_SECRET': 'path/to/client_secret.json',
        'OPENAI_API_KEY': 'your_api_key',
        'PEXELS_API_KEY': 'your_pexels_key'
    }
    for key, placeholder in placeholders.items():
        if os.getenv(key) == placeholder or os.getenv(key) is None:
            return True
    return False

import os
import requests

def download_cat_clips(count=3):
    for i in range(count):
        print(f"Downloading cat clip #{i+1}")

def load_demo_text_snippets(subreddit=None, limit=None):
    return [
        "When your cat gives you side-eye.",
        "Just realized my cat has more followers than me.",
        "This is how my cat judges my life choices."
    ]

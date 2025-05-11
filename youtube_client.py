import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        os.getenv('YOUTUBE_CLIENT_SECRET'),
        scopes=['https://www.googleapis.com/auth/youtube.upload',
                'https://www.googleapis.com/auth/youtube.readonly']
    )
    creds = flow.run_console()
    return build('youtube', 'v3', credentials=creds)

class YouTubeUploader:
    def __init__(self):
        self.service = get_authenticated_service()

    def upload(self, filepath):
        print(f"Uploading {filepath}...")

class YouTubeAnalytics:
    def __init__(self):
        self.service = get_authenticated_service()

    def get_channel_metrics(self):
        return {}

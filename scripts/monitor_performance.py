"""
Fetch and log YouTube analytics; trigger strategy updates
"""
from utils.youtube_client import YouTubeAnalytics

def main():
    analytics = YouTubeAnalytics()
    stats = analytics.get_channel_metrics()
    print(stats)
    # TODO: store in DB and analyze trends

if __name__ == '__main__':
    main()

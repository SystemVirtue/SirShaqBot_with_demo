"""
Upload rendered videos to YouTube via Data API or simulate in DEMO mode.
"""
import os
from utils.config import is_demo_mode
from utils.youtube_client import YouTubeUploader


def main():
    uploader = YouTubeUploader()
    output_dir = 'data/outputs/'
    for video_file in os.listdir(output_dir):
        path = os.path.join(output_dir, video_file)
        if is_demo_mode():
            print(f"DEMO mode: skipping upload for {video_file}")
        else:
            uploader.upload(path)

if __name__ == '__main__':
    main()

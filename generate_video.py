"""
Compose video clips with text overlays and audio, or generate demo outputs.
"""
import os
from utils.config import is_demo_mode
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


def main():
    print("Generating videos...")
    if is_demo_mode():
        clip = VideoFileClip("utils/demo/sample_cat.mp4").subclip(0, 15)
        text = TextClip("This is a demo text snippet", fontsize=40, color='white').set_duration(5).set_position('bottom')
        final = CompositeVideoClip([clip, text])
        final.write_videofile("data/outputs/demo_output.mp4", fps=24)
    else:
        # TODO: implement full generation logic using fetched media and snippets
        pass

if __name__ == '__main__':
    main()

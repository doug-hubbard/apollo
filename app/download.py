import sys
import argparse
import re
from pytube import YouTube


def download(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio = True).first()
    author = yt.author
    title = yt.title
    filename = f"{author}-{title}.mp4"
    clean_file = re.sub('[^A-Za-z0-9 ]+', '', filename)
    audio.download(output_path="downloads",filename=clean_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The full url to a youtube video: https://youtube.com/...")
    args = parser.parse_args()
    download(args.url)
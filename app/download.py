import sys
import argparse
from pytube import YouTube


def download(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio = True).first()
    author = yt.author
    title = yt.title
    audio.download(output_path="downloads",filename=f"{author}-{title}.mp4")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The full url to a youtube video: https://youtube.com/...")
    args = parser.parse_args()
    download(args.url)
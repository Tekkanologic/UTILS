''' 
Simple scripts that downloads videos from youtube.com
Alternative to youtube-dl
DOCS: https://pytube.io/en/latest/

Use env ytdl_env
'''

from pytube import YouTube

link = input("Enter the link: ")

video = YouTube(link, use_oauth=True, allow_oauth_cache=True)

video.streams.filter().first().download()
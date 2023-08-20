"""https://github.com/yt-dlp/yt-dlp"""

from yt_dlp import YoutubeDL

opts = {
    'format': 'bestvideo+bestaudio', 
}

opt_audio = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

URL = input("Enter URL: ")

with YoutubeDL(opt_audio) as ydl:
    ydl.download(URL)
from pytube import YouTube, Playlist
import csv
import os
import subprocess


def merge_audio_and_video(video_file, audio_file, output_file):
    # Construct the FFmpeg command
    cmd = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{output_file}"'

    # Run the FFmpeg command
    subprocess.call(cmd, shell=True)


def Download(link):
    youtubeObject = YouTube(link)
    video_stream = youtubeObject.streams.filter(
        progressive=False, file_extension='mp4').order_by('resolution').desc().first()
    audio_stream = youtubeObject.streams.filter(only_audio=True).first()

    video_file = video_stream.download(filename='video')
    audio_file = audio_stream.download(filename='audio')

    # Replace invalid characters in the filename
    output_file = f"{youtubeObject.title}.mp4"
    for char in [' ', '|', '/', '\\', ':', '*', '?', '"', '<', '>']:
        output_file = output_file.replace(char, '_')

    merge_audio_and_video(video_file, audio_file, output_file)

    os.remove(video_file)
    os.remove(audio_file)

    print("Download is completed successfully")


def download_single_or_playlist(url):
    if "/watch?v=" in url:
        # Single YouTube video URL
        print("Downloading single video:", url)
        Download(url)
    elif "/playlist?list=" in url:
        # YouTube playlist URL
        print("Downloading playlist:", url)
        download_playlist(url)
    else:
        print("Invalid URL:", url)


def download_playlist(playlist_link):
    playlist = Playlist(playlist_link)
    for video_url in playlist.video_urls:
        print("Downloading:", video_url)
        Download(video_url)


# Read links from links.csv file
with open("links.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        url = row[0]
        download_single_or_playlist(url)

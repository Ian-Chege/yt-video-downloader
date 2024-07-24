import csv
import os
import subprocess


def merge_audio_and_video(video_file, audio_file, output_file):
    cmd = f'ffmpeg -i "{video_file}" -i "{
        audio_file}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{output_file}"'
    subprocess.call(cmd, shell=True)


def Download(link):
    cmd_video = f'yt-dlp -f "bestvideo[ext=mp4]" -o "video.mp4" {link}'
    cmd_audio = f'yt-dlp -f "bestaudio[ext=m4a]" -o "audio.m4a" {link}'

    subprocess.call(cmd_video, shell=True)
    subprocess.call(cmd_audio, shell=True)

    output_file = f"output.mp4"
    merge_audio_and_video("video.mp4", "audio.m4a", output_file)

    os.remove("video.mp4")
    os.remove("audio.m4a")

    print("Download is completed successfully")


def download_single_or_playlist(url):
    if "/watch?v=" in url:
        print("Downloading single video:", url)
        Download(url)
    elif "/playlist?list=" in url:
        print("Downloading playlist:", url)
        download_playlist(url)
    else:
        print("Invalid URL:", url)


def download_playlist(playlist_link):
    cmd = f'yt-dlp -i -o "%(title)s.%(ext)s" {playlist_link}'
    subprocess.call(cmd, shell=True)


with open("links.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        url = row[0]
        download_single_or_playlist(url)

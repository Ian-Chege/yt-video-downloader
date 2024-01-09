# YouTube Video Downloader

This project is a Python script that uses the Pytube library to download YouTube videos and playlists. The script can download videos at the highest available resolution while still retaining the audio.

According to the Pytube documentation, some streams listed have both a video codec and audio codec, while others have just the video or audio codec. This is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH). In the context of pytube, the implications are for the highest quality streams; you now need to download both the audio and video tracks and then post-process them with software like FFmpeg to merge them. The legacy streams that contain the audio and video in a single file (referred to as "progressive download") are still available, but only for resolutions 720p and below.

Therefore, if you want to download a video at the highest resolution higher thsn 720p, you will need to download the audio and video separately and then merge them using FFmpeg. This script does that for you.

This script also enables you to download a playlist of videos or single videos. If you want to download a playlist, you will need to provide the URL of the playlist. If you want to download a single video, you will need to provide the URL of the video, and put the link in the `links.csv` file. The script will then read the links from the file and download the videos.

## Table of Contents

- Installation
- Usage

## Installation

To use this script, you will need to have Python 3.x installed on your computer. You will also need to install the Pytube library and FFmpeg.

You can install the Pytube library using pip:

`pip install pytube`

You can install FFmpeg by following the instructions on the [FFmpeg website] or by using a package manager such as [Chocolatey].

`choco install ffmpeg-full`

## Usage

To use this script, you will need to create a file named `links.csv` in the same directory as the script. This file should contain a list of YouTube video or playlist URLs that you want to download, with one URL per line.

Once you have created the `links.csv` file, you can run the script by navigating to the script's directory in a terminal or command prompt and running the following command:

`python main.py`

This will download all of the YouTube videos and playlists listed in the `links.csv` file.

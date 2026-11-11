<div align="center">

# YouTube Downloader

**A command line tool that downloads YouTube videos as MP4 or extracts the audio as MP3.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/built%20with-yt--dlp-red)
![Windows | macOS | Linux](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-555)

</div>

A single Python script built on [yt-dlp](https://github.com/yt-dlp/yt-dlp). Give it a YouTube URL and it saves the video or the audio to a folder, with a progress line that shows percentage, speed and a smoothed ETA.

## Features

- Download a video as MP4 (best available quality by default).
- Extract the audio and convert it to MP3 at 192 kbps.
- Pick a maximum quality: `best`, `worst`, or a height such as `720p` or `1080p`.
- Show a video's title, uploader, duration, views and the start of its description without downloading.
- Save to any folder; the default is `downloads/`, created automatically.
- Accepts `youtube.com` and `youtu.be` links and rejects anything else.

## Getting started

### Prerequisites

- Python 3.11 or newer (current yt-dlp releases require it)
- [FFmpeg](https://ffmpeg.org/download.html) on your PATH. It is needed for MP3 conversion and for merging the separate video and audio streams YouTube uses for higher quality MP4s.

Install FFmpeg with your package manager:

```bash
winget install ffmpeg          # Windows
brew install ffmpeg            # macOS
sudo apt install ffmpeg        # Ubuntu / Debian
sudo pacman -S ffmpeg          # Arch
```

### Install

```bash
git clone https://github.com/AlexMakesC0de/youtube-downloader.git
cd youtube-downloader
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python youtube_downloader.py URL [-f {mp4,mp3}] [-q QUALITY] [-o OUTPUT] [--info]
```

| Option | Default | Meaning |
| --- | --- | --- |
| `url` | | YouTube video URL (quote it in your shell) |
| `-f`, `--format` | `mp4` | `mp4` for video, `mp3` for audio only |
| `-q`, `--quality` | `best` | `best`, `worst`, or a maximum height like `720p` (MP4 only) |
| `-o`, `--output` | `downloads` | Folder to save files in |
| `--info` | | Print video details and exit without downloading |

Examples:

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -f mp3
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -q 720p -o my_videos
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --info
```

Files are named after the video title. The script exits with code 0 on success and 1 on failure.

## Troubleshooting

- **"yt-dlp is not installed"**: activate the virtual environment (you should see `(venv)` in your prompt), then run `pip install -r requirements.txt`.
- **"externally-managed-environment"** on Linux: your distribution protects the system Python. Use the virtual environment from the install steps.
- **FFmpeg not found**: install FFmpeg and open a new terminal so the PATH change applies.
- **"Unable to extract video data"**: check the URL, note that private or region-locked videos cannot be downloaded, and update yt-dlp with `pip install --upgrade yt-dlp`. YouTube changes often, and a newer yt-dlp usually fixes it.

## Disclaimer

This tool is for personal use. Respect YouTube's Terms of Service and copyright law, and only download videos you have the right to download.

## License

[MIT](LICENSE)

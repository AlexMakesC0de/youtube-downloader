# YouTube Downloader

A command-line tool to download YouTube videos as MP4 or extract audio as MP3.

## Features

- Download YouTube videos in MP4 format
- Extract audio and save as MP3
- Choose video quality (best, worst, 720p, 1080p, etc.)
- View video information without downloading
- Custom output directories

## Requirements

- Python 3.7 or higher
- FFmpeg (required for MP3 conversion, so skip if not needed)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-video-downloader.git
cd youtube-video-downloader
```

### 2. Create and activate a virtual environment

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg is required for audio extraction and conversion.

**Arch Linux:**
```bash
sudo pacman -S ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH, or use:
```bash
winget install ffmpeg
```

### 5. You're ready to go!

Make sure your virtual environment is activated (you should see `(venv)` in your terminal prompt) before running the downloader.

**To deactivate the virtual environment later:**
```bash
deactivate
```

**To reactivate it:**
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## Usage

### Basic Commands

**Download video as MP4 (default):**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download audio as MP3:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -f mp3
```

**Download video with specific quality:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -f mp4 -q 720p
```

**Download to custom directory:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" -o my_videos
```

**View video information without downloading:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --info
```

### Command-Line Options

```
positional arguments:
  url                   YouTube video URL

optional arguments:
  -h, --help            Show help message and exit
  -f, --format {mp4,mp3}
                        Download format (default: mp4)
  -q, --quality QUALITY
                        Video quality: best, worst, 720p, 1080p, etc. (default: best)
  -o, --output OUTPUT   Output directory (default: downloads)
  --info                Show video information without downloading
```

## Examples

Download best quality video:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Download 720p video:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4 -q 720p
```

Extract audio as MP3:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp3
```

Download to specific folder:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o ~/Music
```

Check video details first:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --info
```

## Project Structure

```
youtube-video-downloader/
│
├── youtube_downloader.py    # Main application script
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── LICENSE                  # MIT License
└── downloads/               # Default download directory (created automatically)
```

## Troubleshooting

### "externally-managed-environment" Error
This happens on modern Linux distributions (Arch, Ubuntu 23.04+, etc.) that protect system Python.

**Solution:** Always use a virtual environment (see Installation step 2):
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Virtual environment not activated
If you get "yt-dlp is not installed" but you installed it, make sure your virtual environment is activated. You should see `(venv)` in your terminal prompt.

**Activate it:**
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### "yt-dlp is not installed" Error
Make sure your virtual environment is activated, then run: `pip install yt-dlp`

### "FFmpeg not found" Error (for MP3 downloads)
Install FFmpeg using the instructions in the Installation section.

### "Unable to extract video data" Error
- Check if the URL is correct
- The video might be private or region-restricted
- Try updating yt-dlp: `pip install --upgrade yt-dlp`

### Download is very slow
- Check your internet connection
- Try a different quality setting
- The video's server might be slow

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download videos you have the right to download. The developers are not responsible for any misuse of this tool.

## Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)

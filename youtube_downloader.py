#!/usr/bin/env python3
"""
YouTube Video Downloader
A simple and efficient tool to download YouTube videos in MP4 or MP3 format.
"""

import os
import sys
import argparse
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)


class YouTubeDownloader:
    """Handle YouTube video downloads with various options."""
    
    def __init__(self, output_path='downloads'):
        """
        Initialize the downloader.
        
        Args:
            output_path: Directory where downloads will be saved
        """
        self.output_path = Path(output_path)
        self.output_path.mkdir(exist_ok=True)
    
    def download_video(self, url, format_type='mp4', quality='best'):
        """
        Download a YouTube video.
        
        Args:
            url: YouTube video URL
            format_type: 'mp4' for video or 'mp3' for audio only
            quality: Download quality ('best', 'worst', or specific resolution)
        
        Returns:
            bool: True if download successful, False otherwise
        """
        try:
            if format_type.lower() == 'mp3':
                return self._download_audio(url)
            else:
                return self._download_video_mp4(url, quality)
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def _download_video_mp4(self, url, quality):
        """Download video in MP4 format."""
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': str(self.output_path / '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'progress_hooks': [self._progress_hook],
            'quiet': False,
            'no_warnings': False,
        }
        
        if quality != 'best':
            if quality == 'worst':
                ydl_opts['format'] = 'worst[ext=mp4]/worst'
            else:
                # For specific quality like '720p', '1080p'
                height = quality.replace('p', '')
                ydl_opts['format'] = f'bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}][ext=mp4]/best'
        
        print(f"📥 Downloading video as MP4...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"✅ Successfully downloaded: {Path(filename).name}")
            print(f"📁 Saved to: {self.output_path.absolute()}")
            return True
    
    def _download_audio(self, url):
        """Download audio and convert to MP3."""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(self.output_path / '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [self._progress_hook],
            'quiet': False,
            'no_warnings': False,
        }
        
        print(f"🎵 Downloading audio as MP3...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # The filename will have .mp3 extension after post-processing
            base_filename = ydl.prepare_filename(info)
            mp3_filename = Path(base_filename).stem + '.mp3'
            print(f"✅ Successfully downloaded: {mp3_filename}")
            print(f"📁 Saved to: {self.output_path.absolute()}")
            return True
    
    def _progress_hook(self, d):
        """Display download progress."""
        if d['status'] == 'downloading':
            if 'total_bytes' in d:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                print(f"\rProgress: {percent:.1f}%", end='', flush=True)
            elif '_percent_str' in d:
                print(f"\rProgress: {d['_percent_str']}", end='', flush=True)
        elif d['status'] == 'finished':
            print("\n⏳ Processing...", flush=True)
    
    def get_video_info(self, url):
        """
        Get information about a YouTube video without downloading.
        
        Args:
            url: YouTube video URL
        
        Returns:
            dict: Video information
        """
        ydl_opts = {'quiet': True}
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'uploader': info.get('uploader'),
                    'views': info.get('view_count'),
                    'description': info.get('description', '')[:200] + '...',
                }
        except Exception as e:
            print(f"❌ Error getting video info: {str(e)}")
            return None


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Download YouTube videos in MP4 or MP3 format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -f mp3
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -f mp4 -q 720p
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -o my_videos
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID --info
        """
    )
    
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-f', '--format', 
                       choices=['mp4', 'mp3'], 
                       default='mp4',
                       help='Download format (default: mp4)')
    parser.add_argument('-q', '--quality',
                       default='best',
                       help='Video quality: best, worst, 720p, 1080p, etc. (default: best)')
    parser.add_argument('-o', '--output',
                       default='downloads',
                       help='Output directory (default: downloads)')
    parser.add_argument('--info',
                       action='store_true',
                       help='Show video information without downloading')
    
    args = parser.parse_args()
    
    # Validate URL
    if 'youtube.com' not in args.url and 'youtu.be' not in args.url:
        print("❌ Error: Please provide a valid YouTube URL")
        sys.exit(1)
    
    downloader = YouTubeDownloader(output_path=args.output)
    
    # Show info only
    if args.info:
        print("📊 Fetching video information...")
        info = downloader.get_video_info(args.url)
        if info:
            print(f"\n📺 Title: {info['title']}")
            print(f"👤 Uploader: {info['uploader']}")
            print(f"⏱️  Duration: {info['duration']} seconds")
            print(f"👁️  Views: {info['views']:,}")
            print(f"📝 Description: {info['description']}")
        sys.exit(0)
    
    # Download video
    print(f"🚀 Starting download...")
    print(f"📍 URL: {args.url}")
    print(f"📄 Format: {args.format.upper()}")
    if args.format == 'mp4':
        print(f"🎬 Quality: {args.quality}")
    print()
    
    success = downloader.download_video(args.url, args.format, args.quality)
    
    if success:
        print("\n🎉 Download completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Download failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()

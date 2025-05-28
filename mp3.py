import os
import argparse
import yt_dlp

def download_playlist_as_mp3(playlist_url, output_dir="./downloads", bitrate="320"):
    """
    Download all videos from a YouTube playlist as MP3 files at specified bitrate.
    
    Args:
        playlist_url (str): URL of the YouTube playlist
        output_dir (str): Directory to save the MP3 files
        bitrate (str): Audio bitrate in kbps, default is "320"
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Configuration for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'verbose': False,
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': True,  # Skip videos that can't be downloaded
        'noplaylist': False,   # Process the playlist
        'extract_flat': False, # Extract all videos in the playlist
        'writethumbnail': False,
        'writeinfojson': False,
        'writedescription': False,
    }
    
    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([playlist_url])
        
    if error_code == 0:
        print("\nPlaylist download completed successfully!")
    else:
        print(f"\nPlaylist download completed with some errors. Error code: {error_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube playlist videos as MP3s")
    parser.add_argument("playlist_url", help="URL of the YouTube playlist")
    parser.add_argument("-o", "--output", default="./downloads", help="Output directory for MP3 files")
    parser.add_argument("-b", "--bitrate", default="320", help="Audio bitrate in kbps (default: 320)")
    
    args = parser.parse_args()
    # playlist_url = https://www.youtube.com/playlist?list=PL1KFFrJTkUrOVqixTEfG9eDFir4gKlvmx
    download_playlist_as_mp3(args.playlist_url, args.output, args.bitrate)
    
    
    # python mp3.py "https://www.youtube.com/playlist?list=PL1KFFrJTkUrO18tKrEJnXxwI9L_Bd11kU" -o "./Punjabi_S"
    # python mp3.py "https://www.youtube.com/playlist?list=PL1KFFrJTkUrOWSpFrbxDbY2WIMy17kHA-" -o "./MusicN" --verbose
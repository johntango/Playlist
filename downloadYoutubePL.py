import os
import yt_dlp

def download_youtube_playlist(playlist_url, output_folder="downloads"):
    """
    Downloads an entire YouTube playlist using yt-dlp.
    
    :param playlist_url: URL of the YouTube playlist.
    :param output_folder: Directory where downloaded videos will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best quality available
        'outtmpl': f"{output_folder}/%(title)s.%(ext)s",  # Save format
        'noplaylist': False,  # Ensure we download the whole playlist
        'ignoreerrors': True,  # Skip errors instead of stopping
        'merge_output_format': 'mp4',  # Merge video and audio if needed
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert all videos to MP4
        }],
    }

    # Start downloading
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
playlist_url = "https://music.youtube.com/playlist?list=PLyc17goyYFs--zLReyX3-U2T5L2yKtfiK&si=a-UxYkiBosjKVe3a"
download_youtube_playlist(playlist_url)

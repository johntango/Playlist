import json
import time
import pygame
import os

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_song_path(title, artist, music_data):
    """Find the file path of a song based on its title and artist."""
    for song in music_data:
        #if song["title"].lower() == title.lower() and song["artist"].lower() == artist.lower():
        if song["title"] == title:
            return song["file_location"]  # Ensure file_path exists in johnMusic.json
    return None

def play_song(file_path):
    """Play a song using pygame."""
    if os.path.exists(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        # Wait for the song to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    else:
        print(f"File not found: {file_path}")

def play_playlist(music_file, playlist_file):
    """Play songs from the playlist while skipping cortinas."""
    music_data = load_json(music_file)
    playlist_data = load_json(playlist_file)

    for tanda in playlist_data:
        if tanda["type"].lower() == "cortina":
            print("Skipping cortina...")
            continue  # Ignore cortina sections

        for song in tanda["songs"]:
            title, artist = song["title"], song["artist"]
            file_path = find_song_path(title, artist, music_data)

            if file_path:
                print(f"Playing: {title} by {artist}")
                play_song(file_path)
                print("Finished playing. Taking a 10-second break...\n")
                time.sleep(10)  # 10-second break
            else:
                print(f"Song not found: {title} by {artist}")

# File paths
music_file = "johnMusic.json"  # JSON with title, artist, and file_path
playlist_file = "tango_tandas.json"  # JSON with the tanda structure

# Play the playlist
play_playlist(music_file, playlist_file)

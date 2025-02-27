import json
from rapidfuzz import process, fuzz

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Saved {len(data)} songs to {filename}.")

def extract_tanda_songs(tandas):
    """Extracts all song names from the tandas structure."""
    songs = []
    for tanda in tandas:
        extracted_songs = tanda.get("songs", [])
        print(f"Extracted songs from tanda: {extracted_songs}")
        songs.extend(extracted_songs)
    return songs

def find_best_match(song_name, available_songs):
    """Finds the best fuzzy match for a song name."""
    match, score, _ = process.extractOne(song_name, available_songs, scorer=fuzz.partial_ratio)
    if score >= 80:  # Threshold for a good match
        print(f"Matched '{song_name}' with '{match}' (Score: {score})")
        return match
    print(f"No good match found for '{song_name}'")
    return None

def filter_songs():
    tandas_data = load_json("songsTandas.json")  # Nested playlist structure
    john_music = load_json("johnMusic.json")  # List of available songs (dictionaries)
    
    john_song_names = {song["song_name"] for song in john_music}  # Extract song names
    print(f"John's available songs: {john_song_names}")
    available_songs = []
    unmatched_songs = []
    
    for category, data in tandas_data.get("playlist", {}).items():
        print(f"Processing category: {category}")
        for tanda in data.get("tandas", []):
            songs_in_tanda = tanda.get("songs", [])
            print(f"Checking tanda songs: {songs_in_tanda}")
            for song in songs_in_tanda:
                best_match = find_best_match(song, john_song_names)
                if best_match:
                    available_songs.append(best_match)
                else:
                    available_songs.append("missing @@@"+ song)
                    unmatched_songs.append(song)
    
    save_json("milonga.json", available_songs)
    save_json("noMatch.json", unmatched_songs)
    print(f"{len(available_songs)} songs added to milonga.json")
    print(f"{len(unmatched_songs)} songs did not find a match and were saved to noMatch.json")

if __name__ == "__main__":
    filter_songs()

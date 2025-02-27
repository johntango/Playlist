import json

def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def filter_songs():
    playlist = load_json("playlist.json")  # List of song names
    john_music = load_json("johnMusic.json")  # List of available songs
    
    available_songs = [song for song in playlist if song in john_music]
    
    save_json("milonga.json", available_songs)
    print(f"{len(available_songs)} songs added to milonga.json")

if __name__ == "__main__":
    filter_songs()

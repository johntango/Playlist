import json
def remove_duplicates(input_file, output_file):
    # Load the JSON data from the input file
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Use a set to track unique (title, artist) pairs
    seen = set()
    unique_songs = []

    for song in data:
        key = (song["song_name"].lower(), song["singer"].lower())  # Convert to lowercase to avoid case-sensitive duplicates
        if key not in seen:
            seen.add(key)  # Add the key to the set
            
            song = dict(song)  # Create a copy to avoid modifying the original
            # keep all the keys but rename the key "song_name" to "title" and "singer" to "artist" and make sure these are the first two keys in the object. THe order of the other keys does not matter
            song["title"] = song.pop("song_name")
            song["artist"] = song.pop("singer")
            # Add the new keys to the front of the dictionary
            song = {"title": song["title"], "artist": song["artist"], **song}
            # Remove the "song_name" and "singer" keys
            song.pop("song_name", None)
            song.pop("singer", None)
         
        
            # Add the song to the unique list
            unique_songs.append(song)
        else:
            print(f"Duplicate found: {song['song_name']} by {song['singer']}")

    # Save the cleaned JSON data to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(unique_songs, f, indent=2, ensure_ascii=False)

# Example usage
input_file = "johnMusic.json"  # Replace with your actual input file
output_file = "cleaned_johnMusic.json"  # Replace with your desired output file
remove_duplicates(input_file, output_file)

print(f"Duplicates removed. Cleaned file saved as {output_file}.")
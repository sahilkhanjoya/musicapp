
import pandas as pd
songs_df = pd.read_csv('song/routes/data/updated_songs_with_corrected_types.csv')
def search_songs_by_prompt(prompt: str):
    prompt = prompt.lower()
    result = []
    
    # Check for mood or type-based songs like "play sad songs" or "I want to listen sad songs"
    if "sad" in prompt:
        filtered = songs_df[songs_df['Mood_Tag'].str.lower().str.contains("sad")]
    elif "romantic" in prompt:
        filtered = songs_df[songs_df['Mood_Tag'].str.lower().str.contains("romantic")]
    elif "party" in prompt:
        filtered = songs_df[songs_df['Mood_Tag'].str.lower().str.contains("party")]
    elif "play" in prompt and "by" in prompt:
        # Check for "play <song> by <artist>"
        song_part = prompt.split("play")[1].split("by")[0].strip()
        artist_part = prompt.split("by")[1].strip()

        # Search for the song by both name and artist
        filtered = songs_df[(songs_df['Song Name'].str.lower().str.contains(song_part)) &
                            (songs_df['Singer Name'].str.lower().str.contains(artist_part))]
    elif "play" in prompt and "'s songs" in prompt:
        # Check for "play <artist>'s songs"
        artist_part = prompt.split("play")[1].split("'s songs")[0].strip()

        # Search for songs by the artist
        filtered = songs_df[songs_df['Singer Name'].str.lower().str.contains(artist_part)]
    else:
        result.append({"error": "Input format not recognized."})
        return result

    # If songs are found, prepare the result
    if not filtered.empty:
        for _, row in filtered.iterrows():
            song_data = {
                "song_name": row['Song Name'],
                "artist": row['Singer Name'],
                "audio_url": row['Song Audio']
            }
            result.append(song_data)
    else:
        result.append({"error": "No songs found matching the query."})
    
    return result

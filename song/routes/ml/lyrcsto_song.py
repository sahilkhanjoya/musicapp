import pandas as pd
from song.routes.ml.ml import suggest_song
file_path = 'song/routes/data/testsongdata.csv'

def find_song_by_lyrics(snippet):
    # Read the CSV file
    song_data = pd.read_csv(file_path)
    song_data.columns = song_data.columns.str.strip()
    
    # Convert the lyrics and snippet to lowercase
    snippet = snippet.lower()  # Make the snippet lowercase
    song_data['lyrics'] = song_data['lyrics'].str.lower()  # Convert the 'lyrics' column to lowercase
    
    # Perform a search for the lyrics snippet
    matching_songs = song_data[song_data['lyrics'].str.contains(snippet, na=False)]
    
    return matching_songs[['songs']].reset_index(drop=True)


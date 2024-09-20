import pandas as pd

# Load the dataset
file_path = 'song/routes/data/updated_songs_with_corrected_types.csv'
songs_df = pd.read_csv(file_path)

def get_songs_by_type(song_type):
    # Filter the DataFrame for songs based on Final_Type matching the user input
    filtered_songs = songs_df[songs_df['Final_Type'].str.contains(song_type, case=False)]
    
    # Return relevant columns: Song Name, Singer Name, and Song Audio
    return filtered_songs[['Song Name', 'Singer Name', 'Song Audio']]

# Ask user for input on the type of song they want
song_type_prompt = input("Which type of song do you want to listen to? (e.g., Sad, Romantic, Other): ")



# Fetch the songs based on the input type
songs_list = get_songs_by_type(song_type_prompt)

# Display the first few songs of the selected type
if not songs_list.empty:
    print(f"Here are some {song_type_prompt} songs:")
    print(songs_list)
else:
    print(f"Sorry, no {song_type_prompt} songs found.")

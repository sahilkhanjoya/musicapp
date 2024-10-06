import re
from song.routes.ml.mainml import (
    searchbyLyrics, getSongsByEmotion, getSongbySingerSong, playsongbySinger,
    playsongFromMovie, searchSongBySongName, toRatingSongsbyEmotion, suggestmemostEmotionongsBySinger
)

def customNLP(prompt):
    prompt = prompt.lower().strip()
    
    # Play specific songs by a singer
    if "play" in prompt:
        if "songs by" in prompt:
            pattern = r"play songs by\s*(?P<singer>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return playsongbySinger(match.group('singer').strip())
        
        # Play songs based on emotion
        elif "songs" in prompt:
            pattern = r"play\s*(?P<emotion>[A-Za-z\s]+)\s*songs"
            match = re.search(pattern, prompt)
            if match:
                return getSongsByEmotion(match.group('emotion').strip())
        
        # Play specific song by a singer
        elif "by" in prompt:
            pattern = r"play\s*(?P<songname>[A-Za-z\s]+)\s*by\s*(?P<singer>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return getSongbySingerSong(match.group('singer').strip(), match.group('songname').strip())
        
        # Play song from a movie
        elif "from the movie" in prompt:
            pattern = r"play\s*(?P<songname>[A-Za-z\s]+)\s*from the movie\s*(?P<movie>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return playsongFromMovie(match.group('songname').strip(), match.group('movie').strip())
        
        # Play a song by name
        else:
            pattern = r"play\s*(?P<songname>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return searchSongBySongName(match.group('songname').strip())
    
    # Suggest best songs by emotion
    elif "suggest" in prompt:
        if "best" in prompt and "songs" in prompt:
            pattern = r"suggest me best\s*(?P<emotion>[A-Za-z\s]+)\s*songs"
            match = re.search(pattern, prompt)
            if match:
                return toRatingSongsbyEmotion(match.group('emotion').strip())
        
        # Suggest most emotional songs by singer
        elif "most" in prompt and "song by" in prompt:
            pattern = r"suggest me most\s*(?P<emotion>[A-Za-z\s]+)\s*song by\s*(?P<singer>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return suggestmemostEmotionongsBySinger(match.group('emotion').strip(), match.group('singer').strip())

    # If none of the above, search by lyrics
    return searchbyLyrics(prompt)


# import spacy
# from fuzzywuzzy import fuzz, process

# # Load the small English NLP model
# nlp = spacy.load("en_core_web_sm")

# # Music data for songs, playlists, and genres
# songs = {
#     "Shape of You": "Ed Sheeran",
#     "Blinding Lights": "The Weeknd",
#     "Levitating": "Dua Lipa",
#     "Bohemian Rhapsody": "Queen",
#     "Hotel California": "Eagles",
#     "Someone Like You": "Adele",
#     "Bad Guy": "Billie Eilish",
#     "Smells Like Teen Spirit": "Nirvana",
#     "Uptown Funk": "Mark Ronson ft. Bruno Mars"
# }

# playlists = {
#     "Workout Playlist": ["Lose Yourself - Eminem", "Eye of the Tiger - Survivor", "Stronger - Kanye West"],
#     "Relaxing Playlist": ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit", "Clair de Lune - Debussy"],
#     "Top Hits 2024": ["Levitating - Dua Lipa", "Blinding Lights - The Weeknd", "Bad Habits - Ed Sheeran"]
# }

# genres = {
#     "Pop": ["Shape of You", "Levitating", "Blinding Lights", "Bad Guy"],
#     "Rock": ["Bohemian Rhapsody", "Hotel California", "Smells Like Teen Spirit"],
#     "Classical": ["Moonlight Sonata - Beethoven", "Clair de Lune - Debussy", "Canon in D - Pachelbel"]
# }

# user_preferences = {
#     "last_played_song": None,
#     "last_played_playlist": None,
#     "last_played_genre": None
# }

# def get_best_match(user_input, data):
#     """ Use fuzzy matching to find the best match for the user query. """
#     match, score = process.extractOne(user_input, data.keys(), scorer=fuzz.partial_ratio)
#     if score > 70:
#         return match
#     return None

# def extract_genre(doc):
#     """ Extract the genre or category from the user input using NLP. """
#     for token in doc:
#         if token.pos_ == "NOUN" or token.pos_ == "PROPN":
#             return token.text.lower()
#     return None

# def analyze_user_input(user_input):
#     """ Use NLP to analyze the user input and extract relevant information. """
#     doc = nlp(user_input)

#     # Look for keywords related to songs, playlists, or genres
#     for ent in doc.ents:
#         if ent.label_ in ("WORK_OF_ART", "PERSON"):
#             return ent.text, "song"

#     genre = extract_genre(doc)
#     if genre in genres:
#         return genre, "genre"
    
#     return None, "unknown"

# def get_music_data(user_input):
#     """ Determine what the user wants based on their input. """
#     user_input = user_input.lower()  # Convert input to lowercase
#     doc = nlp(user_input)

#     entity, entity_type = analyze_user_input(user_input)

#     # Check for song requests
#     if entity_type == "song":
#         best_song_match = get_best_match(entity, songs)
#         if best_song_match:
#             user_preferences['last_played_song'] = best_song_match
#             return f"Playing '{best_song_match}' by {songs[best_song_match]}."

#     # Check for playlist requests
#     best_playlist_match = get_best_match(user_input, playlists)
#     if best_playlist_match:
#         user_preferences['last_played_playlist'] = best_playlist_match
#         playlist_tracks = "\n".join(playlists[best_playlist_match])
#         return f"Playing {best_playlist_match}:\n{playlist_tracks}"

#     # Check for genre requests
#     best_genre_match = get_best_match(user_input, genres)
#     if best_genre_match:
#         user_preferences['last_played_genre'] = best_genre_match
#         genre_tracks = "\n".join(genres[best_genre_match])
#         return f"Playing {best_genre_match} music:\n{genre_tracks}"

#     # Recommendations based on preferences
#     if "recommend" in user_input or "suggest" in user_input:
#         if user_preferences['last_played_genre']:
#             return f"Since you like {user_preferences['last_played_genre']} music, here are more songs:\n" + "\n".join(genres[user_preferences['last_played_genre']])
#         return "I can recommend music based on what you like. Try asking for a song or genre first!"

#     # Handling follow-up queries like "play something similar"
#     if "similar" in user_input or "like" in user_input:
#         if user_preferences['last_played_song']:
#             artist = songs[user_preferences['last_played_song']]
#             return f"Playing more songs like {user_preferences['last_played_song']} by {artist}."

#     return "Sorry, I couldn't find what you're looking for. Please try again with a different query."

# def main():
#     print("Welcome to the advanced music player!")
#     print("You can ask to play a song, a playlist, or a genre.")
    
#     while True:
#         user_input = input("\nWhat would you like to listen to? (Type 'exit' to quit) ")

#         if user_input.lower() == 'exit':
#             print("Goodbye!")
#             break

#         # Get response based on user input
#         response = get_music_data(user_input)
#         print(response)

# if __name__ == "__main__":
#     main()

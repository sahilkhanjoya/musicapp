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

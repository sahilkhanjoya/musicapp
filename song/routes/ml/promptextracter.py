import re
from song.routes.ml.mainml import searchbyLyrics, getSongsByEmotion, getSongbySingerSong, playsongbySinger, playsongFromMovie, searchSongBySongName, toRatingSongsbyEmotion, suggestmemostEmotionongsBySinger


def customNLP(prompt):
    prompt = prompt.lower()
    if "play" in prompt:
        if "play songs by" in prompt:
            print("check 1")
            pattern = r"play songs by\s*(?P<singer>[A-Za-z\s]+)"
    
            match = re.search(pattern, prompt)
            if match:
              return  playsongbySinger(match.group('singer').strip())
            return None
        elif "play" in prompt and "songs" in prompt:
            print("check 2")
            pattern = r"play\s*(?P<emotion>[A-Za-z\s]+)\s*songs"
            match = re.search(pattern, prompt)
            if match:
                return getSongsByEmotion(match.group('emotion').strip()) 
            
            return None
        elif  "play"in prompt and "by" in prompt:
            pattern = r"play\s*(?P<songname>[A-Za-z\s]+)\s*by\s*(?P<singer>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
               return getSongbySingerSong(match.group('singer').strip(), match.group('songname').strip())
            
            return None
        elif r"play" in prompt and "from the movie" in prompt:
            print("check 3")
            pattern =r"play\s*(?P<songname>[A-Za-z\s]+)\s*from the movie\s*(?P<movie>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                
               return playsongFromMovie(match.group('songname').strip(), match.group('movie').strip())
            return None
        elif "play" in prompt:
            pattern = r"play\s*(?P<songname>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
               return searchSongBySongName(match.group('songname').strip())
            return None
    
    elif "suggest" in prompt:
        if "suggest me best" in prompt and "songs" in prompt:
            pattern  = r"suggest me best\s*(?P<emotion>[A-Za-z\s]+)\s*songs"
            match = re.search(pattern, prompt)
            if match:
               return toRatingSongsbyEmotion(match.group('emotion').strip())
              
            return None
        elif "suggest me most" in prompt and "song by" in prompt:
            print("check 4")
            pattern  = r"suggest me most\s*(?P<emotion>[A-Za-z\s]+)\s*song by\s*(?P<singer>[A-Za-z\s]+)"
            match = re.search(pattern, prompt)
            if match:
                return suggestmemostEmotionongsBySinger(match.group('emotion').strip(), match.group('singer').strip())
            return None
                
            
    elif  "suggest me best" in prompt and "songs" in prompt:
        print("Check 2")
        pattern  = r"suggest me best\s*(?P<emotion>[A-Za-z\s]+)\s*songs"
        match = re.search(pattern, prompt)
        if match:
            return toRatingSongsbyEmotion(match.group('emotion').strip())
        return None
    else:
        return searchbyLyrics(prompt)
        
            



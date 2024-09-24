import librosa
import numpy as np

# Function to load and compute the MFCC (Mel-frequency cepstral coefficients) for a given audio file
def extract_mfcc(audio_path):
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return np.mean(mfcc, axis=1)

# Function to compare two audio files using cosine similarity
def cosine_similarity(mfcc1, mfcc2):
    return np.dot(mfcc1, mfcc2) / (np.linalg.norm(mfcc1) * np.linalg.norm(mfcc2))

# Load the small clip
small_clip_path = '097fcb02-6d64-4836-ad0f-976718326e1e.mp3'
small_clip_mfcc = extract_mfcc(small_clip_path)

# List of song URLs or paths
song_paths = [
    'https://work-pool.blr1.digitaloceanspaces.com/socialMedia_songs/89959dbf-ee37-4613-99e4-25514167cd54.mp3', 
    'https://work-pool.blr1.digitaloceanspaces.com/socialMedia_songs/784faae9-1015-4ec2-94d0-3a1284e77a39.mp3', 
    'https://work-pool.blr1.digitaloceanspaces.com/socialMedia_songs/097fcb02-6d64-4836-ad0f-976718326e1e.mp3']  # Add your song links or paths here

# Variable to keep track of the best match
best_match = None
best_similarity = -1

# Compare the small clip with each song
for song_path in song_paths:
    try:
        song_mfcc = extract_mfcc(song_path)
        similarity = cosine_similarity(small_clip_mfcc, song_mfcc)
        print(f"Similarity with {song_path}: {similarity}")

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = song_path

    except Exception as e:
        print(f"Error processing {song_path}: {e}")

# Print the best match
if best_match:
    print(f"The song that best matches the small clip is: {best_match} with a similarity score of {best_similarity}")
else:
    print("No matching song found.")

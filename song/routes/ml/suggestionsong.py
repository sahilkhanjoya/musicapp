import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV file (replace with your actual file path)
file_path = 'song/routes/data/traindatagener.csv'


# Function to recommend songs based on a song title
def get_recommendations(song_title):
    df = pd.read_csv(file_path)

    # Clean up the columns if necessary (removing extra spaces, etc.)
    df.columns = df.columns.str.strip()
    
    # Fill missing genres with 'Unknown'
    df['genri'] = df['genri'].fillna('Unknown')
    
    # Combine lyrics and genre into one string for content-based filtering
    df['combined_features'] = df['lyrics'].fillna('') + ' ' + df['genri'].fillna('')
    
    # Initialize a TF-IDF Vectorizer (to vectorize the text data)
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    
    # Vectorize the combined features (lyrics + genre)
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])
    
    # Compute the cosine similarity matrix based on the TF-IDF vectors
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get the index of the song that matches the song_title
    idx = df.index[df['songs'].str.lower() == song_title.lower()].tolist()
    
    if not idx:
        return "Song not found!"
    
    idx = idx[0]

    # Get the pairwise similarity scores of all songs with the given song
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the songs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top 30 most similar songs
    sim_scores = sim_scores[1:30]  # Skip the first one as it's the same song

    # Get the song indices
    song_indices = [i[0] for i in sim_scores]

    # Return the top 30 most similar songs (without indices)
    return df['songs'].iloc[song_indices].tolist()

# Example usage: Recommend songs similar to 'Kun Faya Kun'



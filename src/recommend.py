import joblib
import logging
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recommend.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("Loading data...")
try:
    df = joblib.load('df_cleaned.pkl')
    tfidf_matrix = joblib.load('tfidf_matrix.pkl')
    cosine_sim = joblib.load('cosine_sim.pkl')
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    logging.info("Data loaded successfully.")
except Exception as e:
    logging.error("Failed to load required files: %s", str(e))
    raise e


def recommend_songs(song_name, top_n=5, mood=None):
    # recommend songs based on lyrical simiarity
    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        logging.warning("Song not found in dataset.")
        return None
    idx = idx[0]  # first match of the song : if there are multiple
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    song_indices = [i[0] for i in sim_scores]
    result_df = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result_df.index = result_df.index + 1
    result_df.index.name = "Rank"
    return result_df


def recommend_by_mood(text, top_n=5):
    # recommend songs based on user mood description
    if not text.strip():
        return None
    # create TF-IDF vector for the input text

    mood_vector = tfidf_vectorizer.transform([text])
    tfidf_existing = tfidf_matrix
    # similarity between mood text and all lyrics
    sim_scores = cosine_similarity(mood_vector, tfidf_existing)[0]
    top_indices = sim_scores.argsort()[-top_n:][::-1]
    recommendations = df[['artist', 'song']].iloc[top_indices].reset_index(drop=True)
    recommendations.index = recommendations.index + 1
    recommendations.index.name = "Rank"
    return recommendations

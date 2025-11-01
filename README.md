🎵 Music Recommendation System

This is a Streamlit web application that recommends songs either by lyrics similarity or by user mood.
It uses TF-IDF vectorization and cosine similarity on song lyrics data to find related songs.

🚀 Features

🎶 Lyrics-based recommendation:
Select a song and get similar tracks based on lyrical meaning.

😊 Mood-based recommendation:
Describe how you feel, and the app will recommend songs that match your mood.

⚡ Machine Learning pipeline:
Uses TF-IDF and cosine similarity to compute semantic similarity between lyrics.

🧠 Preprocessing included:
The dataset is cleaned, tokenized, and vectorized automatically.

🧩 Installation

Clone this repository

git clone https://github.com/your-username/music-recommendation.git
cd music-recommendation


Create and activate a virtual environment

On Windows:
python -m venv venv
venv\Scripts\activate

On macOS / Linux:
python3 -m venv venv
source venv/bin/activate


Install all dependencies

pip install -r requirements.txt


Download the Million Song Dataset

The app requires song lyrics data. Download the dataset from Kaggle:
Million Song Dataset

Place the CSV file (e.g., spotify_millsongdata.csv) in the project root folder.

Ensure the file name matches what is used in preprocess.py.

Preprocess the dataset

Run the preprocessing script to clean and vectorize the lyrics:

python preprocess.py


This will generate the following files:

df_cleaned.pkl – Cleaned song data

tfidf_matrix.pkl – TF-IDF vectorized lyrics

tfidf_vectorizer.pkl – TF-IDF vectorizer for mood analysis

cosine_sim.pkl – Cosine similarity matrix
⚙️ Preprocess the Dataset

Before running the app, execute the preprocessing script to prepare the data:

python preprocess.py


This will:

Clean and tokenize lyrics

Compute TF-IDF matrix and cosine similarity

Save all files as .pkl for fast access later

💻 Run the Application

Start the Streamlit app using:

streamlit run app.py


Then open the displayed link (usually http://localhost:8501
) in your browser.

How It Works

Lyrics Recommendation:

Select a song title.

The system finds other songs with high cosine similarity in lyrics.

Mood Recommendation:

Enter your mood or a short text (e.g., “I feel relaxed”).

The system analyzes your text and recommends songs with similar lyrical sentiment.

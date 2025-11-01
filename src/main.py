import streamlit as st
from recommend import df, recommend_songs

# Set custom Streamlit page config
st.set_page_config(
    page_title="Music Recommendation System",
    page_icon="icon.jpg",
    layout="centered"
)


st.title("Music Recommendation System")
st.write("Choose how you want to discover new songs:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Recommend Songs by Lyrics"):
        st.switch_page("pages/lyrics_Recommendation.py")

with col2:
    if st.button("Recommend Songs by Mood"):
        st.switch_page("pages/mood_Recommendation.py")

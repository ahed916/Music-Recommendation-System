import streamlit as st
from recommend import recommend_by_mood

st.set_page_config(page_title="Mood Recommendation", page_icon="icon.jpg",
                   layout="centered")

st.title("Recommend Songs by Mood")

text = st.text_area("How are you feeling today? Describe your mood:")

if st.button("Recommend Songs"):
    with st.spinner("Analyzing your mood and finding songs..."):
        recommendations = recommend_by_mood(text)
        if recommendations is None or recommendations.empty:
            st.warning("No songs found for this mood.")
        else:
            st.success("Here are some songs that match your mood:")
            st.table(recommendations)

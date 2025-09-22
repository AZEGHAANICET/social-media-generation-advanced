import streamlit as st

st.title("AI Social Media Content Generator")

platform = st.selectbox("Platform", ["Instagram", "Twitter", "Facebook", "LinkedIn"])
tone = st.selectbox("Tone", ["Professional", "Casual", "Funny", "Inspirational"])
content_type = st.selectbox("Content Type", ["Caption", "Hashtag", "Post Idea"])
prompt = st.text_area("Prompt", placeholder="What is your post about?")
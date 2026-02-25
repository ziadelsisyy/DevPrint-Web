import streamlit as st
import requests
import pandas as pd
from analyzer import analyze_user

st.set_page_config(page_title="DevPrint", layout="centered")

st.title("🧠 DevPrint")
st.subheader("Discover your GitHub coding personality")

username = st.text_input("Enter GitHub username")

if st.button("Analyze"):

    if username:
        response = requests.get(f"https://api.github.com/users/{username}/repos")

        if response.status_code == 200:
            repos = response.json()
            result = analyze_user(repos)

            st.success("Analysis Complete!")

            st.metric("Total Repositories", result["total_repos"])
            st.metric("Total Stars", result["total_stars"])
            st.metric("Top Language", result["top_language"])

            st.header("👤 Personality Type")
            st.info(result["personality"])

        else:
            st.error("User not found.")

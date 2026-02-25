import streamlit as st
import requests

st.set_page_config(page_title="DevPrint", layout="centered")

st.title("🧠 DevPrint")
st.subheader("Discover your GitHub coding personality")

# دالة تحليل المستخدم
def analyze_user(repos):
    total_repos = len(repos)
    total_stars = 0
    language_count = {}

    for repo in repos:
        if repo["language"]:
            language = repo["language"]
            language_count[language] = language_count.get(language, 0) + 1
        total_stars += repo["stargazers_count"]

    top_language = max(language_count, key=language_count.get) if language_count else "None"

    personality = "Explorer"
    icon = "🧭"

    if total_repos > 20 and total_stars > 10:
        personality = "Architect"
        icon = "🏗️"
    elif total_repos > 30:
        personality = "Hacker"
        icon = "⚡"
    elif len(language_count) > 5:
        personality = "Researcher"
        icon = "🔬"

    return {
        "total_repos": total_repos,
        "total_stars": total_stars,
        "top_language": top_language,
        "personality": personality,
        "icon": icon
    }

# واجهة المستخدم
username = st.text_input("Enter GitHub username")

if st.button("Analyze"):
    if username:
        response = requests.get(f"https://api.github.com/users/{username}/repos")

        if response.status_code == 200:
            repos = response.json()
            result = analyze_user(repos)

            st.success("✅ Analysis Complete!")

            st.metric("Total Repositories", result["total_repos"])
            st.metric("Total Stars", result["total_stars"])
            st.metric("Top Language", result["top_language"])

            st.header(f"{result['icon']} Personality Type")
            st.info(result["personality"])

            st.markdown(f"[View GitHub Profile](https://github.com/{username})")
        else:
            st.error("❌ User not found.")

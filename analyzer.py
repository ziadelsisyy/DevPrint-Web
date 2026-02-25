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

    if total_repos > 20 and total_stars > 10:
        personality = "Architect"
    elif total_repos > 30:
        personality = "Hacker"
    elif len(language_count) > 5:
        personality = "Researcher"

    return {
        "total_repos": total_repos,
        "total_stars": total_stars,
        "top_language": top_language,
        "personality": personality
    }

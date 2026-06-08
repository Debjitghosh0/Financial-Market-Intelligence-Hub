def validate_articles(articles):

    valid_articles = []

    seen_titles = set()

    stats = {
        "missing_title": 0,
        "missing_source": 0,
        "duplicates": 0
    }

    for article in articles:

        if not article.get("title"):
            stats["missing_title"] += 1
            continue

        if not article.get("source"):
            stats["missing_source"] += 1
            continue

        if article["title"] in seen_titles:
            stats["duplicates"] += 1
            continue

        seen_titles.add(article["title"])

        valid_articles.append(article)

    return valid_articles, stats

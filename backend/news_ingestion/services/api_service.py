import requests


def get_market_news(api_key):
    url = f"https://finnhub.io/api/v1/news?category=general&token={api_key}"

    response = requests.get(url)

    articles = response.json()

    cleaned_articles = []

    for article in articles:
        cleaned_articles.append(
            {
                "title": article.get("headline"),
                "source": article.get("source"),
                "published_at": article.get("datetime"),
                "url": article.get("url")
            }
        )

    return cleaned_articles

import requests


def get_market_news(api_key):
    try:
        url = f"https://finnhub.io/api/v1/news?category=general&token={api_key}"

        response = requests.get(url)

        if response.status_code != 200:
            print("API request failed")
            return []

        articles = response.json()

        cleaned_articles = []

        for article in articles:
            cleaned_articles.append(
                {
                    "title": article.get("headline"),
                    "source": article.get("source"),
                    "published_at": article.get("datetime"),
                    "url": article.get("url")
                }
            )

        return cleaned_articles

    except Exception as e:
        print(f"Error: {e}")
        return []

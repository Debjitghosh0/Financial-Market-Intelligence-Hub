import requests

from datetime import datetime

def get_market_news(api_key):
    try:
        url = f"https://finnhub.io/api/v1/news?category=general&token={api_key}"

        response = requests.get(url)

        if response.status_code != 200:
            print(f"API request failed. Status Code: {response.status_code}")
            print(response.text)
            return []

        articles = response.json()

        cleaned_articles = []

        for article in articles:
            cleaned_articles.append(
                {
                    "title": article.get("headline"),
                    "source": article.get("source"),
                    "published_at": datetime.fromtimestamp(
    article.get("datetime")
).strftime("%Y-%m-%d %H:%M:%S"),
                    "url": article.get("url")
                }
            )

        return cleaned_articles

    except Exception as e:
        print(f"Error: {e}")
        return []

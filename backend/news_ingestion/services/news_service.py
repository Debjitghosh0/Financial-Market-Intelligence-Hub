import json

def save_news(news_articles):
    with open("data/raw/news.json", "w") as file:
        json.dump(news_articles, file, indent=4)

from services.api_service import get_market_news
from services.news_service import save_news

API_KEY = "d8irs3hr01qmeaujomegd8irs3hr01qmeaujomf0"

news = get_market_news(API_KEY)

save_news(news)

print(f"Saved {len(news)} articles")

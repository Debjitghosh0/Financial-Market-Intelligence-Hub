from services.api_service import get_market_news
from services.validation_service import validate_articles
from services.news_service import save_news

API_KEY = "d8irs3hr01qmeaujomegd8irs3hr01qmeaujomf0"

news = get_market_news(API_KEY)

print(f"Articles before validation: {len(news)}")

valid_news, stats = validate_articles(news)

print(f"Articles after validation: {len(valid_news)}")

save_news(valid_news)

print("\n----- Pipeline Report -----")

print(f"Total Articles Received : {len(news)}")
print(f"Missing Titles          : {stats['missing_title']}")
print(f"Missing Sources         : {stats['missing_source']}")
print(f"Duplicates Removed      : {stats['duplicates']}")
print(f"Final Valid Articles    : {len(valid_news)}")

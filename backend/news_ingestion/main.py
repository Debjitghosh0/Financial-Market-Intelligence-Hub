from services.api_service import get_market_news
from services.validation_service import validate_articles
from services.news_service import save_news
from services.logging_service import get_logger

logger = get_logger()

API_KEY = "d8irs3hr01qmeaujomegd8irs3hr01qmeaujomf0"
logger.info("Pipeline Started")

news = get_market_news(API_KEY)

print(f"Articles before validation: {len(news)}")

valid_news, stats = validate_articles(news)

logger.info(f"Retrieved {len(news)} articles")

print(f"Articles after validation: {len(valid_news)}")

logger.info("Validation Completed")

save_news(valid_news)

from services.s3_service import upload_file_to_s3

upload_file_to_s3(
    "data/raw/news.json",
    "financial-market-intelligence-hub-debjit",
    "raw/news.json"
)


logger.info(f"Saved {len(valid_news)} valid articles")
logger.info("Pipeline Finished Successfully")
logger.info("Uploaded news.json to S3")

print("\n----- Pipeline Report -----")

print(f"Total Articles Received : {len(news)}")
print(f"Missing Titles          : {stats['missing_title']}")
print(f"Missing Sources         : {stats['missing_source']}")
print(f"Duplicates Removed      : {stats['duplicates']}")
print(f"Final Valid Articles    : {len(valid_news)}")

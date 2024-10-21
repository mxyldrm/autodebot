import os

# Auto.de'ye Special configs
BASE_URL = "https://www.auto.de/search?pageNumber={}&activeSort=NEWEST_OFFERS_FIRST"
RESPONSE_IDENTIFIER = "car-search-endpoint/api/v1/search/car/formatted"
BOT_NAME = "AutoDE Bot"

# Headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Telegram for notification 
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

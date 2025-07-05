import requests
from globals import NEWSAPI_KEY, logger
from datetime import datetime

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ") if isinstance(dt_str, str) else dt_str

def fetch_top_headlines():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "language": "en",
        "pageSize": 100,
        "apiKey": NEWSAPI_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    items = []
    for art in data.get("articles", []):
        items.append({
            "title": art["title"],
            "description": art["description"],
            "url": art["url"],
            "published_at": parse_datetime(art["publishedAt"]),
            "source": art["source"]["name"],
        })
    logger.info(f"Fetched {len(items)} articles.")
    return items

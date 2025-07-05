from globals import celery_app
from app import fetch_top_headlines, helpers
from globals import SessionLocal, Base, engine

Base.metadata.create_all(engine)

#CELERY_BEAT CONFIG
celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "fetch_and_store_news",
        "schedule": 60,
    }
}

@celery_app.task(name="fetch_and_store_news")
def fetch_and_store_news():
    db = SessionLocal()
    try:
        articles = fetch_top_headlines()
        helpers.insert_articles(db, articles)
    finally:
        db.close()

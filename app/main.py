from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from globals import SessionLocal
from app.models import Article

app = FastAPI(title="News Fetcher API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/articles")
def latest_articles(limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Article).order_by(Article.published_at.desc()).limit(limit).all()

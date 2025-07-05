from sqlalchemy.orm import Session
from app.models import Article

def insert_articles(db: Session, articles: list[dict]):
    for a in articles:
        if not db.query(Article).filter_by(url=a["url"]).first():
            db.add(Article(**a))
    db.commit()

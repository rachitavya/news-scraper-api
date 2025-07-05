from sqlalchemy import Column, Integer, String, DateTime, Text, UniqueConstraint
from datetime import datetime
from globals import Base

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512))
    description = Column(Text)
    url = Column(String(255), unique=True)  
    published_at = Column(DateTime)
    source = Column(String(255))
    fetched_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint("url", name="_url_uc"),)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from celery import Celery

import os
import logging, sys
from dotenv import load_dotenv
load_dotenv()

#NEWSAPI_KEY
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")

#DB CONFIG
engine = create_engine(os.getenv("MYSQL_URI"), pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

#CELERY CONFIG
celery_app = Celery(
    "news_tasks",
    broker=os.getenv("CELERY_BROKER"),
)

# Logging CONFIG
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

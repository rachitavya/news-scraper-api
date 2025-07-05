# news-scraper-api
A celery server which fetches news at regular interval and a FastAPI server which retrieves them.

## Quick-start README

This repository ships a lightweight Docker Compose setup that mounts your source code into three identical Python containers built from the same image. Each container installs the dependencies in `requirements.txt`; at runtime they just run the code.

**What each service does:**

* **`beat`** – the Celery Beat scheduler; **every minute it triggers the News API scraper task**, which the worker then processes.
* **`worker`** – a Celery worker that executes the heavy-lifting job of inserting freshly-fetched articles into the database.
* **`api`** – runs FastAPI with Uvicorn at [http://localhost:8000](http://localhost:8000); hit `/articles` to read the news records stored in MySQL.

### Prerequisites

1. **MySQL 8.0+** listening on **port 3306** locally, with a database (e.g. `news_service`) and a user/password that match your `.env` file:
2. **Redis 7+** listening on **port 6379** locally;
3. Docker Engine (or Docker Desktop)

### Launch app

1. Set these [environment variables](sample.env) in a `.env` file, 
2. run: `docker compose up --build`

and all three services will start, sharing the same code and dependencies while talking to your external MySQL and Redis instances.

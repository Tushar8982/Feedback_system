# Feedback Collection System

A Django-based feedback collection system with REST API, JWT authentication, Celery for async tasks, and Telegram bot integration.

## Features
- Submit feedback via REST API
- JWT authentication (public and protected endpoints)
- Celery + Redis for async email sending
- Telegram bot integration (stores usernames)
- Environment variable management

## Setup

1. Clone the repo and install requirements:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your secrets.
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Start Celery worker:
   ```sh
   venv\Scripts\activate
   celery -A feedback_system worker --loglevel=info
   ```
7. Start the Telegram bot:
   ```sh
   python scripts/run_bot.py
   ```

## API Endpoints
- `POST /api/feedback/` — Submit feedback (public)
- `GET /api/feedback/` — List feedback (public)
- `GET /api/feedback/<id>/` — Feedback detail (protected)
- `POST /api/token/` — Obtain JWT
- `POST /api/token/refresh/` — Refresh JWT
- `GET /api/hello/` — Protected hello endpoint

## License
MIT

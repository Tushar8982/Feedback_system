# 🚀 Feedback Collection System

![Django](https://img.shields.io/badge/Django-4.2.2-green?logo=django)
![DRF](https://img.shields.io/badge/DRF-3.14.0-blue?logo=django)
![Celery](https://img.shields.io/badge/Celery-5.3.1-brightgreen?logo=celery)
![Redis](https://img.shields.io/badge/Redis-4.5.5-red?logo=redis)
![Telegram Bot](https://img.shields.io/badge/Telegram%20Bot-20.3-blue?logo=telegram)

---

## ✨ Overview
A modern, production-ready feedback collection system built with Django, Django REST Framework, Celery, Redis, and Telegram Bot integration. Collect feedback from users via API or Telegram, process asynchronously, and manage everything from a secure admin panel.

---

## 🛠️ Features
- 🔒 JWT Authentication (djangorestframework-simplejwt)
- 📝 Feedback submission via REST API & Telegram Bot
- ⚡ Asynchronous email notifications with Celery & Redis
- 🤖 Telegram bot integration (stores users, collects feedback)
- 🛡️ Environment variable support for all secrets
- 🖥️ Django Admin for feedback/user management
- 🐳 Docker-ready (optional)

---

## 📦 Tech Stack
- Django 4.2.2
- Django REST Framework
- Celery + Redis
- PostgreSQL (Supabase-ready)
- Telegram Bot API
- Docker (optional)

---

## 🚦 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Tushar8982/Feedback_system.git
cd Feedback_system
```

### 2. Setup environment
- Copy `.env.example` to `.env` and fill in your secrets.
- Install dependencies:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Database & Migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Start services
- **Start Redis** (from its folder):
  ```
  .\redis-server.exe
  ```
- **Start all project services:**
  ```
  start_all.bat
  ```

### 5. Telegram Bot
- Create a bot with [@BotFather](https://t.me/BotFather) and add the token to `.env`.
- Interact with your bot at [t.me/Internship_feedback_bot](https://t.me/Internship_feedback_bot)

---

## 🌍 Environment Variables
See `.env.example` for all required variables:
- `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- `REDIS_URL`, `TELEGRAM_BOT_TOKEN`

---

## 🧑‍💻 Usage
- Access Django admin: [http://localhost:8000/admin](http://localhost:8000/admin)
- Submit feedback via Telegram or API
- All feedback is visible in admin panel

---

## 🐳 Docker (optional)
- Use `docker-compose up` to run everything in containers (see `docker/` folder)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE)

---

<p align="center">
  <img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" width="200" alt="Feedback Animation"/>
</p>

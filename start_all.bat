@echo off
REM Activate virtual environment
call .\venv\Scripts\activate

REM Start Django server
start cmd /k "python manage.py runserver"

REM Start Celery worker (solo pool)
start cmd /k "celery -A feedback_system worker --loglevel=info --pool=solo"

REM Start Telegram bot
start cmd /k "python scripts\run_bot.py"

echo All services started! Please start Redis manually if not already running.
pause

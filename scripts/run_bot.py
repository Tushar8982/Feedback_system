import os
import sys
from dotenv import load_dotenv
from asgiref.sync import sync_to_async

# Set up Django settings before importing Django modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedback_system.settings')
import django
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from core.models import TelegramUser, Feedback

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

@sync_to_async
def get_or_create_telegram_user(telegram_id, username, first_name=None, last_name=None):
    user, _ = TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    return user

@sync_to_async
def save_feedback(telegram_user, message):
    Feedback.objects.create(user=telegram_user, message=message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_user = await get_or_create_telegram_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )
    name = user.username or user.first_name or "User"
    await update.message.reply_text(f"Hello, {name}! Please send your feedback as a message.")

async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_user = await get_or_create_telegram_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )
    await save_feedback(telegram_user, update.message.text)
    await update.message.reply_text("Thank you for your feedback!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_feedback))
    app.run_polling()

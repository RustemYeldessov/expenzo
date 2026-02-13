import os
import django
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tengecash.settings')
django.setup()

from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async

from tengecash.users.models import User


@sync_to_async
def link_user(tg_id, username):
    try:
        user = User.objects.get(username='admin')
        if not user.telegram_id:
            user.telegram_id = tg_id
            user.save()
            return f'Приятно познакомиться, {user.username}! Твой Telegram привязан.'
        return f'С возвращением, {user.username}!'
    except User.DoesNotExist:
        return "Пользователь не найден."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    message = await link_user(tg_id, update.effective_user.username)
    await update.message.reply_text(message)


if __name__ == '__main__':
    # Читаем токен из переменных окружения
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    print("Бот запущен...")
    application.run_polling()
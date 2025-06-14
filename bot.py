import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from models import init_db

load_dotenv()  # Загружает переменные из .env
TOKEN = os.getenv('TELEGRAM_TOKEN')  # Безопасное получение токена

def start(update, context):
    update.message.reply_text("Добро пожаловать в Budget Keeper!")

def main():
    init_db()  # Инициализация БД
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
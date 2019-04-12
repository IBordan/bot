# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='891538500:AAHBYYQClhnU0aVMxO0AVYAmIbTi9HcNU-E') # Токен API к Telegram
dispatcher = updater.dispatcher
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
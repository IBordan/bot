# ���������
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='891538500:AAHBYYQClhnU0aVMxO0AVYAmIbTi9HcNU-E') # ����� API � Telegram
dispatcher = updater.dispatcher
# �������� ����� ����������
updater.start_polling(clean=True)
# ������������� ����, ���� ���� ������ Ctrl + C
updater.idle()
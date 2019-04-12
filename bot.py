import sys
from settings import *
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='/english - English''\n/ukrainian - Українська мова', parse_mode= 'Markdown')
def startUKR(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='\n*Вас вітає бот "Комп’ютерних наук", спеціальність № 122!*' '\n*Яку інформацію Ви хочете дізнатися?*' '\n\n*Вступ пiсля школи (бакалаврiат):*'
                     '\n /ukraboutcsbach - Інформація про спеціальності'
                     '\n /ukrdocumentsbach - Перелік документів для вступу'
                     '\n /ukrdisciplinesbach - Дисципліни підготовки'
                     '\n /ukrznobach - Предмети ЗНО для вступу'
                     '\n /ukrpostsbach - Посади підготовки'
                     '\n /ukrpricebach - Ціни на контракт'
                     '\n\n*Вступ до магістратури:*'
                     '\n /ukraboutcsms - Інформація про спеціальності'
                     '\n /ukrdocumentsms - Перелік документів для вступу'
                     '\n /ukrexamms - Перелік вступних іспитів'
                     '\n /ukrdisciplinesms - Дисципліни підготовки'
                     '\n /ukrpostsms - Посади підготовки'
                     '\n /ukrpricems - Ціни на контракт'
                     '\n\n *Приймальна комісія ОНПУ:*'
                     '\n Україна, 65044, Одеса, проспект Шевченка, 1' 
                     '\n Телефони: (+38 048) 722-19-94, 705-83-33', parse_mode= 'Markdown')
def startENG(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='\n*You are welcomed by the bot "Computer Sciences", specialty number 122!*' '\n*What information do you want to know?*' '\n\n*Introduction after school (bachelor):*'
                     '\n /engaboutcsbach - Information on specialty'
                     '\n /engdocumentsbach - List of documents for entry'
                     '\n /engdisciplinesbach - Discipline of preparation'
                     '\n /engznobach - ZNO for entry'
                     '\n /engpostsbach - Training places'
                     '\n /engpricebach - Contract prices'
                     '\n\n*Introduction to the magistracy:*'
                     '\n /engaboutcsms - Information on specialty'
                     '\n /engdocumentsms - List of documents for entry'
                     '\n /engexamms - List of entrance exams'
                     '\n /engdisciplinesms - Discipline of preparation'
                     '\n /engpostsms - Training places'
                     '\n /engpricems - Contract prices'
                     '\n\n *Selection committee of ONPU:*'
                     '\n Ukraine, 65044, Odessa, Shevchenko avenue, 1' 
                     '\n Phones: (+38 048) 722-19-94, 705-83-33', parse_mode= 'Markdown')
    # Хендлеры
    start_command_handler = CommandHandler('start', startCommand)
    start_ukr_command_handler = CommandHandler('ukrainian', startUKR)
    start_eng_command_handler = CommandHandler('english', startENG)
    # Добавляем хендлеры в диспетчер
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(start_ukr_command_handler)
    dispatcher.add_handler(start_eng_command_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()

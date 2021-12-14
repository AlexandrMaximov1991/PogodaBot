import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)


class ComandsBot:
    @bot.message_handler(commands=['help'])
    def start(self, message: telebot.types.Message):
        text = f"Для работы бота, просто введи название населенного пункта." \
               f""
        bot.reply_to(message, text)

    @bot.message_handler(commands=['start'])
    def start(self, message: telebot.types.Message):
        text = f"Привет,этот бот сделан для того,\n" \
               f"чтобы ты всегда был одет по погоде.\n" \
               f"Чтобы узнать как бот работает ,\n" \
               f"нажми:/help."
        bot.reply_to(message, text)

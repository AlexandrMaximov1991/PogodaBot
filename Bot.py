import telebot
import requests
from config import TOKEN, appid

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def start(message: telebot.types.Message):
    text = f"Для работы бота, просто введи название населенного пункта." \
           f""
    bot.reply_to(message, text)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f"Привет,этот бот сделан для того,\n" \
           f"чтобы ты всегда был одет по погоде.\n" \
           f"Чтобы узнать как бот работает ,\n" \
           f"нажми:/help."
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def answer(message: telebot.types.Message):
    s_city = message.text.split()

    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                       params={'q': s_city,
                               'units': 'metric',
                               'lang': 'ru',
                               'APPID': appid,
                               })
    data = res.json()

    try:
        True
    except Exception as e:
        bot.reply_to(message, f'Ошибка {e}, попробуйте позже.',
                     )

    try:
        a = data['weather'][0]['description']
    except KeyError:
        bot.reply_to(message, f'Не удалось обработать город {s_city}, попробуйте еще раз.',
                     )

    else:

        b = float(data['main']['temp'])
        c = float(data['main']['temp_min'])
        d = float(data['main']['temp_max'])
        e = data['main']['humidity']
        f = float(data['main']['feels_like'])
        g = float(data['wind']['speed'])
        h = float(data['wind']['gust'])
        # q =

        text1 = f'Погода в городе {s_city} {a}\n' \
            f'Температура теперь {round(b)}°C\n' \
            f'Ощущается как {round(f)}°C\n' \
            f'Относительная влажность воздуха {e}%\n' \
            f'Скорость ветра {round(g)} м/с\n' \
            f'С порывами до {round(h)} м/с '

        text = f'Погода в городе {s_city} {a}\n' \
            f'Температура теперь: {round(b)}°C\n' \
            f'Ощущается как {round(f)}°C\n' \
            f'Минимальная температура: {round(c)}°C\n' \
            f'Максимальная температура: {round(d)}°C\n' \
            f'Относительная влажность воздуха: {e}%\n' \
            f'Скорость ветра {round(g)} м/с\n' \
            f'С порывами до {round(h)} м/с '
        if round(b) == round(c) and round(c) == round(d):
            bot.send_message(message.chat.id, text1,
                             )
        else:
            bot.send_message(message.chat.id, text,
                             )


bot.polling()

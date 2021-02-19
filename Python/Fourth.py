from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import telebot

owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()
bot = telebot.TeleBot("1660750835:AAHGqW8re60Cdm1ByyhEzzQif-QEEXQqbWU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
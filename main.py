import os
import telebot
from datetime import datetime
import pytz



my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey, Hows it going?")

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['date'])
def date(message):
    utc = pytz.utc
    pst = pytz.timezone('America/Los_Angeles')
    ist = pytz.timezone('Asia/Calcutta')
    pt = pytz.timezone('Europe/London')
    bot.send_message(message.chat.id, f'Current Date Time in UTC = {datetime.now(tz=utc)}')
    bot.send_message(message.chat.id, f'Current Date Time in PST = {datetime.now(pst)}')
    bot.send_message(message.chat.id, f'Current Date Time in IST = {datetime.now(ist)}')
    bot.send_message(message.chat.id, f'Current Date Time in BST = {datetime.now(pt)}',)


bot.polling()

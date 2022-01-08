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
    utc_string = datetime.now(tz=utc)
    pst_string = datetime.now(pst)
    ist_string = datetime.now(ist)
    pt_string = datetime.now(pt)
    bot.send_message(message.chat.id, f'Current Date Time in UTC = {utc_string.strftime("%A, %d. %B %Y %I:%M%p")}')
    bot.send_message(message.chat.id, f'Current Date Time in PST = {pst_string.strftime("%A, %d. %B %Y %I:%M%p")}')
    bot.send_message(message.chat.id, f'Current Date Time in IST = {ist_string.strftime("%A, %d. %B %Y %I:%M%p")}')
    bot.send_message(message.chat.id, f'Current Date Time in BST = {pt_string.strftime("%A, %d. %B %Y %I:%M%p")}',)


bot.polling()

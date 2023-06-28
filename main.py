import telebot
from random import randint
import json
from telebot import types
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    token = data["token"]
    bot = telebot.TeleBot(token)


def user_checker(id_):
    ids = open("id.txt", "r").read()
    splitting_ids = ids.split()
    if str(id_) not in splitting_ids:
        open("id.txt", 'w').write(f"{str(id_)} ")


def simen():
    print("lol")

@bot.message_handler(commands=['start'])
def commands(m):
    mrkup = types.InlineKeyboardMarkup()
    mrkup.add(types.InlineKeyboardButton("потеребить ананас", callback_data=f"simen"))
    bot.send_message(m.from_user.id, 'helo', reply_markup=mrkup)
    user_checker(m.from_user.id)

@bot.callback_query_handler(func=lambda callback: True)
def cumback(callback):
    if callback.data == "simen":
        commands(callback)

bot.infinity_polling()
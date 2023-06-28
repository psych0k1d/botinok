import telebot
from random import randint
import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    token = data["token"]
    bot = telebot.TeleBot(token)


def user_checker(id_):
    ids = open("id.txt", "r").read()
    splitting_ids = ids.split()
    if str(id_) not in splitting_ids:
        open("id.txt", 'w').write(f"{str(id_)} ")


@bot.message_handler(commands=['start'])
def commands(m):
    bot.send_message(m.from_user.id, 'helo')
    user_checker(m.from_user.id)


bot.infinity_polling()
import telebot
import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    token = data["token"]

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def commands(m):
    bot.send_message(m.from_user.id, 'helo')



bot.infinity_polling()
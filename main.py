import os
import telebot
import csv
import random

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.send_message('Welcome!')


@bot.message_handler(commands=['truth'])
def truth(message):
    with open('truth.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        bot.reply_to(message, rows[random.randint(1, 41)])


@bot.message_handler(commands=['dare'])
def dare(message):
    with open('dare.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        bot.reply_to(message, rows[random.randint(1, 89)])


bot.polling()

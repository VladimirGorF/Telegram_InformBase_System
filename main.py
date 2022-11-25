import sqlite3
import datetime
import telebot
import data_base
import addition_modul
import change_module
import deletion_modul
import search_and_return_module



API_TOKEN = 


bot = telebot.TeleBot(API_TOKEN)
print('Server started')


@bot.message_handler(commands=['start'])
def help_message(message):
    bot.send_message(message.chat.id,f"/showAll\n/showOne\n/delete\n/change\n/add")


@bot.message_handler(commands=['showAll'])
def help_message(message):
    bot.send_message(message.chat.id,f"Здесь вся база {XXXXXXXX} ")



#
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if 'привет' in message.text:
#         bot.send_message(message.chat.id, 'и тебе привет')


bot.polling()

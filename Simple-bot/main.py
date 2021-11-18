#@Gadzhiyavov_Dzhamal_bot
import telebot
import random
from telebot import types
token = "2050558050:AAGem-8GDNc5Wb6YGHFYyxyq7gcIAcCKx6E"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею много чего.\n'
                                      'Список команд:\n'
                                      '/start - Начать диалог\n'
                                      '/randomnumb - рандомное число от 0 до 1000\n'
                                      '/search - искать что-то\n'
                                      '/whoami - who am i? действительно\n'
                                      'Также можешь спросить у меня, например, "кто я?", "сколько тебе лет?", "ты умный?"\n')
@bot.message_handler(commands=['randomnumb'])
def start_message(message):
    bot.send_message(message.chat.id, random.randint(0,1000))
@bot.message_handler(commands=['search'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ищу.... Ищу....... ничего не нашел(')
@bot.message_handler(commands=['whoami'])
def start_message(message):
    bot.send_message(message.chat.id, "i don't know")
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "кто я?":
        bot.send_message(message.chat.id, 'Я даже не знаю кто я, а ты спрашиваешь кто ты...')
    if message.text.lower() == "сколько тебе лет?":
        bot.send_message(message.chat.id, '0, я родился всего-то 18 ноября')
    if message.text.lower() == "ты умный?":
        bot.send_message(message.chat.id, 'В отличии от тебя - да')
bot.polling()
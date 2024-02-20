# Задание 2
# Реализуйте механизм «Орел или Решка». Пользователь
# загадывает орла или решку. Чат-бот случайным образом
# выбирает орла или решку. Если выбор пользователя совпал с результатом, он выиграл, иначе проиграл.
# Используйте API сайта random.org. Подробнее об
# использовании API читайте тут https://api.random.org/.

import telebot
import requests
from telebot import types

bot = telebot.TeleBot('6516763960:AAGjJgu4c6ZdEVRMRjvUYZgh9F72LNJ0XZs')
API_KEY = 'e1823b1e-eb37-4045-b17c-edd853508b1e'


def get_coin_flip():
    url = f'https://api.random.org/json-rpc/2/invoke'
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
        "apiKey": API_KEY,
        "n": 1,
        "min": 0,
        "max": 1,
        "replacement": True
        },
        "id": 42
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    coin_flip = result['result']['random']['data'][0]
    return coin_flip


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Начать работу")
    markup.add(random_sender)
    bot.send_message(message.chat.id, f'Приветствую {message.from_user.first_name}')
    bot.send_message(message.chat.id, 'Выберете о или р')


@bot.message_handler(content_types=['text'])
def coin_flip_game(message):
    user_choice = message.text.lower()
    if user_choice not in ['о', 'р']:
        bot.send_message(message.chat.id, "Некорректный выбор. Попробуйте еще раз.")
    else:
        coin = get_coin_flip()
        if (coin == 0 and user_choice == 'о') or (coin == 1 and user_choice == 'р'):
            bot.send_message(message.chat.id, "Вы угадали! Вы выиграли.")
        else:
            bot.send_message(message.chat.id, "Вы не угадали. Попробуйте еще раз.")


bot.polling(none_stop=True)

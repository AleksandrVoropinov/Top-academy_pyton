# Задание 3
# Реализуйте механизм «Игральные кости». Чат-бот и
# пользователь по очереди бросают кости. Побеждает тот,
# кто выбросит большую сумму. Реализовать интерфейс
# для запуска новой игры. При броске нужно отображать
# количество очков на каждом кубике.
# Используйте API сайта random.org. Подробнее об
# использовании API читайте тут https://api.random.org/.

import telebot
import requests
from telebot import types

bot = telebot.TeleBot('6516763960:AAGjJgu4c6ZdEVRMRjvUYZgh9F72LNJ0XZs')
API_KEY = 'e1823b1e-eb37-4045-b17c-edd853508b1e'


def roll_dice():
    url = f'https://api.random.org/json-rpc/2/invoke'
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": API_KEY,
            "n": 2,
            "min": 1,
            "max": 6,
            "replacement": True
            },
        "id": 42
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if "result" in data:
        dice1 = data["result"]["random"]["data"][0]
        dice2 = data["result"]["random"]["data"][1]
        total = dice1 + dice2
        return dice1, dice2, total
    else:
        return None


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Приветствую {message.from_user.first_name}')
    bot.send_message(message.chat.id, "Добро пожаловать в игру 'Игральные кости'!")
    bot.send_message(message.chat.id, "Введите любое сообщение чтобы кинуть кости'!")


@bot.message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def display_roll(message):
    dice1, dice2, total = roll_dice()
    bot.send_message(message.chat.id, f"Первый кубик: {dice1}")
    bot.send_message(message.chat.id, f"Второй кубик: {dice2}")
    bot.send_message(message.chat.id, f"Сумма очков: {total}")


bot.polling(none_stop=True)

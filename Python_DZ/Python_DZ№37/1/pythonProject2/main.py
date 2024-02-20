# Создайте чат-бота, который позволит пользователю
# получить функциональность, описанную ниже.
# Задание 1
# Пользователь выбирает начало и конец диапазона,
# количество чисел. Чат-бот генерирует набор случайных
# чисел на основании, пользовательских данных.
# Используйте API сайта random.org. Подробнее об
# использовании API читайте тут https://api.random.org/

import telebot
import requests
from telebot import types

bot = telebot.TeleBot('6516763960:AAGjJgu4c6ZdEVRMRjvUYZgh9F72LNJ0XZs')
API_KEY = 'e1823b1e-eb37-4045-b17c-edd853508b1e'

def get_random_number(minimum, maximum):
    url = f'https://api.random.org/json-rpc/2/invoke'
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
        "apiKey": API_KEY,
        "n": 1,  # Number of random integers to generate
        "min": minimum,
        "max": maximum,
        "replacement": True
        },
    "id": 42
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()['result']['random']['data'][0]
    return result


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Начать работу")
    markup.add(random_sender)
    bot.send_message(message.chat.id, f'Приветствую {message.from_user.first_name} данный бот может сгенерировать рандомное число для тебя')
    bot.send_message(message.chat.id, '👇Нажми на кнопку ниже что бы начать работу👇', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def first_number_step(message):
    if message.text == 'Начать работу':
        msg = bot.send_message(message.chat.id, 'Введите начало диапазона')
        bot.register_next_step_handler(msg, second_number_step)
    else:
        bot.send_message(message.chat.id, 'Такой команды нет')


def second_number_step(message):
    global NUM_first
    NUM_first = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
    bot.register_next_step_handler(msg, result_number_step)


def result_number_step(message):
    global NUM_second
    NUM_second = int(message.text)
    result(message)


def result(message):
    random_number = get_random_number(NUM_first, NUM_second)
    bot.send_message(message.chat.id, 'Случайное число: ' + str(random_number))


bot.polling(none_stop=True)

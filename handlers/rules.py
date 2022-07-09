from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config
from datetime import datetime
import json
import requests

def btc():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key)
    data = data.json()
    return f"{data['symbol']} Цена {data['price']}$"

@dp.message_handler()
async def echo(message: types.Message):

    match message.text.lower():
        case "/инфо" | "/info" | "/information":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "/номета" | "/nometa":
            await message.answer("\n[Пожалуйста, не задавайте мета-вопросов в чате!](https://nometa.xyz/)", parse_mode='markdown')
        case "/get_message_id":
            await message.answer(message.chat.id)
        case "/инфа":
            await message.answer("[\n* Клуб дедов-программистов FAQ *\n\nВ этом репозитории находится полезная информация, собранная участниками чата. Дорожные карты(roadmaps), шпаргалки, ссылки на курсы и самые полезные статьи.\n\nЭлементарный уровень\n - Начало работы с Вебом\n - Язык программирования Python\n - Введение в программирование. Подборка материалов по остальным языкам.\n\nПродвинутый уровень\n - Все для веб-разработчика\n - Все для Python-разработчика\n - Пет-проекты разной сложности: ресурсы, идеи\n - Задачи для прокачки + тестовые задания\n\nМатериалы и ресурсы других ИТ-сообществ:\n - Что учить веб-разработчику. Разные гайды 2021\n - Карты развития Python 2021\n\nПрофессии\n - В тестировщики хочу, пусть меня научат!\n - Кто такие бизнес-аналитики и как стать БА?\n\nПолезное:\n - Git и GitHub\n - Как мы учим английский язык](https://github.com/OldCodersClub/faq)", parse_mode='markdown', disable_web_page_preview=True)
        case "алиса сколько времени?":
            await message.answer(datetime.now())
        case "курс биткойна?":
            await message.answer(btc())

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")
    elif "алиса, сколько время?" in message.text.lower():
        await message.answer("Э, слушай, так некультурно говорить")
    elif "алиса, сколько времени?" in message.text.lower():
        await message.answer("По гринвичу "+datetime.today().strftime("%H ч %M мин"))
    elif "алиса, который час?" in message.text.lower():
        await message.answer("Mikko Kukanen, это ты такой культурный? По гринвичу"+datetime.today().strftime("%H ч %M мин"))



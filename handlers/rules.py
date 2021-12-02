from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config


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

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")


# @dp.message_handler(text=["/инфо", "/info"])
# async def text_in_handler(message: types.Message):
#     await message.answer("https://github.com/OldCodersClub/faq")

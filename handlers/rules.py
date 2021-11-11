from aiogram import types
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text.lower():
        case "/инфо" | "/info":
            await message.answer("https://github.com/OldCodersClub/faq")

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")

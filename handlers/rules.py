from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text:
        case "/инфо" | "/info" | "/инфа" | "/information":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "/get_message_id":
            await message.answer(message.chat.id)

    if "привет деды" in message.text:
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")


# @dp.message_handler(text=["/инфо", "/info"])
# async def text_in_handler(message: types.Message):
#     await message.answer("https://github.com/OldCodersClub/faq")

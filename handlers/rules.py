from aiogram import types
from aiogram.dispatcher.webhook import SendMessage
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text.lower():
        case "/инфо" | "/info":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "/secret":
            await message.answer(message.chat.id)
        case "/secret2":
            return SendMessage(reply_to_message_id=-780574242, text="DEMO")

    if "привет деды" in message.text.lower():
        await message.answer("И тобе привет Cтарина")
    elif "вступил(а) в группу" in message.text.lower():
        await message.answer("Добро пожаловать\nСоветуем ознакомиться с дедовским архивом знаний\n\n\nhttps://github.com/OldCodersClub/faq")


# @dp.message_handler(text=["/инфо", "/info"])
# async def text_in_handler(message: types.Message):
#     await message.answer("https://github.com/OldCodersClub/faq")

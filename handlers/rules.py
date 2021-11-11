from aiogram import types
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text:
        case "/инфо" | "/info":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "привет":
            await message.answer("И тобе привет старина")

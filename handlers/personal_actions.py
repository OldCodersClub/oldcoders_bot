from aiogram import types
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):

    match message.text:
        case "/инфо":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "привет Деды":
            await message.answer("И тобе привет старина")
        case "/secret":
            await message.answer("{c}")

    # if message.text == "/инфо":
    #     await message.answer("https://github.com/OldCodersClub/faq")
    # else:
    #     await message.answer(message.text)

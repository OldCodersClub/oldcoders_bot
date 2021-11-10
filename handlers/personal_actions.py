from aiogram import types
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "/инфо":
        await message.answer("https://github.com/OldCodersClub/faq")
    # else:
    #     await message.answer(message.text)

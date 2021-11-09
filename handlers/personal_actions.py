from aiogram import types
from dispatcher import dp
import config


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "hello":
        await message.answer("thx - good day")
    else:
        await message.answer(message.text)

import os
from aiogram import types
from dispatcher import dp
import config
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['BOT_TOKEN'], os.environ['BOT_OWNER'])


@dp.message_handler()
async def echo(message: types.Message):

    match message.text:
        case "/инфо":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "привет Деды":
            await message.answer("И тобе привет старина")
        case "/secret":
            await message.answer("{s3}")

    # if message.text == "/инфо":
    #     await message.answer("https://github.com/OldCodersClub/faq")
    # else:
    #     await message.answer(message.text)

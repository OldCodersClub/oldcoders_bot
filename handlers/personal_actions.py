from aiogram import types
from dispatcher import dp
import config
from config import s3 as s3


@dp.message_handler()
async def echo(message: types.Message):

    match message.text:
        case "/инфо":
            await message.answer("https://github.com/OldCodersClub/faq")
        case "привет Деды":
            await message.answer("И тобе привет старина")
        case "/secret":
            await message.answer(f'{s3}')

    # if message.text == "/инфо":
    #     await message.answer("https://github.com/OldCodersClub/faq")
    # else:
    #     await message.answer(message.text)

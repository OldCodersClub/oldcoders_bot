from aiogram import Bot, Dispatcher, executor, types
import config
import logging

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "hello":
        await message.answer("thx - good day")
    else:
        await message.answer(message.text)


# run long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

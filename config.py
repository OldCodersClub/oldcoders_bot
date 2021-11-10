import os


async def token():
    s3 = await os.environ.get('BOT_TOKEN')
    return s3

BOT_TOKEN = token()
BOT_OWNER = "oldcoders_bot"

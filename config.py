from environs import Env
# import os

env = Env()
env.read_env()

# BOT_TOKEN2 = str(os.environ.get('BOT_TOKEN'))
BOT_OWNER = "oldcoders_bot"

BOT_TOKEN = "2111338135:AAGhltOYCNaitXNwY0jh4z2A-3ba2-VgBVU"


BOT_TOKEN2 = env.str("BOT_TOKEN")

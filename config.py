import os
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['BOT_TOKEN'])


# group ids or account ids can be retrieved with @username_to_id_bot
BOT_TOKEN = "2111338135:AAGhltOYCNaitXNwY0jh4z2A-3ba2-VgBVU"
BOT_OWNER = "oldcoders_bot"

# s3 = S3Connection(os.environ['BOT_TOKEN'], os.environ['BOT_OWNER'])

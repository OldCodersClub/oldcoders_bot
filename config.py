# from boto.s3.connection import S3Connection
# # s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

# # BOT_TOKEN = S3Connection(os.environ['BOT_TOKEN'])
# BOT_OWNER = "oldcoders_bot"
# BOT_TOKEN = S3Connection(security_token='BOT_TOKEN')

import boto
c = boto.connect_s3()
BOT_TOKEN = c.get_bucket('BOT_TOKEN')
# BOT_OWNER = c.get_bucket('BOT_OWNER')

# group ids or account ids can be retrieved with @username_to_id_bot
# BOT_TOKEN = "2111338135:AAGhltOYCNaitXNwY0jh4z2A-3ba2-VgBVU"
BOT_OWNER = "oldcoders_bot"

# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

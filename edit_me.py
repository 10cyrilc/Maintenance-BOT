# © Cyril C Thomas
# © https://t.me/c_text_bot
# © https://t.me/c_bots_support



import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","") #Get this from @BOTfather
    API_ID = int(os.environ.get("API_KEY", )) # Get this from my.telegram.org
    API_HASH = os.environ.get("API_HASH","") # Get this from my.telegram.org

    BOT_TEXT = os.environ.get("BOT_TEXT","") # Comment this out if using default text
    #Hello {} , This Bot Is Currently Under Maintenance.\n\nYou Can't Use This Bot Right Now.\n\nI Will Post a Message On This Updates Channel If This Bot Is Up.
    CHANNEL_LINK = os.environ.get("CHANNEL_LINK","") # Link of Your Channel
    DEV_ID = os.environ.get("DEV_ID","") # Your Username without @

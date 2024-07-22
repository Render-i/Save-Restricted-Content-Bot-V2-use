# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "4478313"))
API_HASH = getenv("API_HASH", "e4ebfd81dc38ea54e879a51cf52b28c2")
BOT_TOKEN = getenv("BOT_TOKEN", "6705455229:AAGktvt9t3J28_ZMcwS7svuHZFERWNyhufs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7267794879").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://formangodb2blip763:hellomango2@mymain.yjvosiy.mongodb.net/?retryWrites=true&w=majority&appName=Mymain")
LOG_GROUP = getenv("LOG_GROUP", "2229932987")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2180203045"))

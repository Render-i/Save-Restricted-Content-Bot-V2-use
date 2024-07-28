# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21503676"))
API_HASH = getenv("API_HASH", "6c480b0a5221c80a5bda833c4bea259c")
BOT_TOKEN = getenv("BOT_TOKEN", "7238867445:AAGePHfsyGLiJotJg-qRLXkn6HZ4h3Z_b64")
OWNER_ID = int(getenv("OWNER_ID", "7396928828"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://formangodb2blip763:hellomango2@mymain.yjvosiy.mongodb.net/?retryWrites=true&w=majority&appName=Mymain")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002219822240"))
FORCESUB = getenv("FORCESUB", "hellochannelforfun")

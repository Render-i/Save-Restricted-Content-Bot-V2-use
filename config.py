# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23937359"))
API_HASH = getenv("API_HASH", "b5667982a25e4f8706e4ac75f92f995a")
BOT_TOKEN = getenv("BOT_TOKEN", "7296574210:AAHTP0QAVOr5QbvZ9bIFDQix5cLdep3789E")
OWNER_ID = int(getenv("OWNER_ID", "7315008850"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://formangodb2blip763:hellomango2@mymain.yjvosiy.mongodb.net/?retryWrites=true&w=majority&appName=Mymain")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002246457581"))
FORCESUB = getenv("FORCESUB", "channelforyusl")

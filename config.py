# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28777147"))
API_HASH = getenv("API_HASH", "d2bc9a3b9121ea859fd1c69bcb5ddaea")
BOT_TOKEN = getenv("BOT_TOKEN", "7423618582:AAHtmCs9uqQxJTv3pikR-OGRVqupe9Hg-ik")
OWNER_ID = int(getenv("OWNER_ID", "7218244733"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://formangodb2blip763:hellomango2@mymain.yjvosiy.mongodb.net/?retryWrites=true&w=majority&appName=Mymain")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002229718376"))
FORCESUB = getenv("FORCESUB", "canhhell")

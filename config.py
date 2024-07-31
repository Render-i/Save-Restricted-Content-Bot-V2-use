# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20559409"))
API_HASH = getenv("API_HASH", "b144bbcb6fdfd51cc4002482063aa975")
BOT_TOKEN = getenv("BOT_TOKEN", "6823706593:AAHritO9gpz55KJ0daj0rU4udzglvh-YCaI")
OWNER_ID = int(getenv("OWNER_ID", "7377441452"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://formangodb2blip763:hellomango2@mymain.yjvosiy.mongodb.net/?retryWrites=true&w=majority&appName=Mymain")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002229718376"))
FORCESUB = getenv("FORCESUB", "cgatle)

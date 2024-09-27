from aiogram import Bot, Dispatcher
from data import config
from baza.sqlite import Database
from aiogram.enums import ParseMode


ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

commands = ["/start", "/about", "/help", "/admin"]

bot = Bot(TOKEN)
db = Database(path_to_db="main.db")
dp = Dispatcher()
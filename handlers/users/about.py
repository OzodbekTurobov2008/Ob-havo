from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bot dan shikoyatingiz yoki taklifingiz bo'lsa📜\n👤Admin tugmasini bosing va xabaringizni yozib qoldiring✅\n\nBotdan foydalanish tartibi👇🏻\n/start - Botni ishga tushurish \n /hepl - Bot haqida Malumot\nOb-havo botdan o'zingizga kerakli viloyatni tanlang🙂")


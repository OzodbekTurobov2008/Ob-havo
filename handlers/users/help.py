from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("🔥 Buyruqlar \nBotdan foydalanish uchun ... \n/start - Botni ishga tushurish\n /about - Bot haqida \n\nAdmin bilan bog'lanmoqchi bo'lsangiz \"👤Admin\" tugmasini bosing va ✉️ Xabaringizni yozib qoldiring ! ")

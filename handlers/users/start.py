from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.weather_inl_b import weather_inl_button

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, Ob-Havo botimizga hush kelibsiz", reply_markup=weather_inl_button)
    except:
        await message.answer(text="Assalomu alaykum", reply_markup=weather_inl_button)

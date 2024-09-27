from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.weather_inl_b import weather_inl_button
from keyboard_buttons.admin_keyboard import admin_button1
from aiogram.fsm.context import FSMContext


@dp.message(CommandStart())
async def start_command(message:Message,state:FSMContext):
 
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz🙂\nBu bot orqali siz viloyatlarni topishingiz mumkin!✅", reply_markup=weather_inl_button)
        await state.clear()
    except:
        await message.answer(text="Assalomu alaykum", reply_markup=weather_inl_button)
        await message.answer(text="👨‍💼Admin bilan bog'lanish uchun\nAdminga xabar tugmasini bosing✅", reply_markup=admin_button1)
        await state.clear()
        
from loader import dp, bot
from aiogram import F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboard_buttons.weather_inl_b import weather_inl_button, sozlamalar, sozlamalarni_ichi
from weather import get_weather
from days import get_weather_forecast

# Tashkent
@dp.callback_query(F.data=="Tashkent")
async def Toshkent(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Tashkent"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Navoi
@dp.callback_query(F.data=="Navoi")
async def Navoi(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Navoi"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Samarkand
@dp.callback_query(F.data=="Samarkand")
async def Samarkand(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Samarkand"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Namangan
@dp.callback_query(F.data=="Namangan")
async def Namangan(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Namangan"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Jizzakh
@dp.callback_query(F.data=="Jizzakh")
async def Jizzakh(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Jizzakh"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Nukus
@dp.callback_query(F.data=="Nukus")
async def Nukus(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Nukus"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Zarafshan
@dp.callback_query(F.data=="Zarafshan")
async def Zarafshan(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Zarafshan"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Bukhara
@dp.callback_query(F.data=="Bukhara")
async def Bukhara(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Bukhara"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Sirdaryo
@dp.callback_query(F.data=="Sirdaryo")
async def Sirdaryo(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Sirdaryo"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Fergana
@dp.callback_query(F.data=="Fergana")
async def Fergana(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Fergana"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)
    
# Andijan
@dp.callback_query(F.data=="Andijan")
async def Andijan(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Andijan"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Urgench
@dp.callback_query(F.data=="Urgench")
async def Urgench(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Urgench"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)

# Termiz
@dp.callback_query(F.data=="Termiz")
async def Termiz(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Termiz"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)



# Khiva
@dp.callback_query(F.data=="Khiva")
async def Khiva(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    city_name = "Khiva"
    await state.update_data(city_name = city_name)
    await callback.message.answer(text="Qanday ob-havo ma'lumotini olishni istaysiz?",reply_markup=sozlamalar)
    

# qo'shimcha

@dp.callback_query(F.data=="kun")
async def sozlama(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    data = await state.get_data()
    city_name = data.get("city_name")
    weather = get_weather(city_name)

    response = (f"Bugun, {weather['date']}\n\n"
                f"Hozir: ☀️ +{weather['current_temp']}°, ↖️ {weather['wind_speed']:.1f} m/s\n\n"
                f"Tong: {weather['day_forecast']['Tong']}\n"
                f"Kun: {weather['day_forecast']['Kun']}\n"
                f"Oqshom: {weather['day_forecast']['Oqshom']}\n"
                f"Namlik: {weather['humidity']}%\n"
                f"Shamol: {weather['wind_direction']}, {weather['wind_speed']:.1f} m/s\n"
                f"Bosim: {weather['pressure']} mm sim. ust.\n\n"
                f"Oy: {weather['moon_phase']}\n"
                f"Quyosh chiqishi: {weather['sunrise']}\n"
                f"Quyosh botishi: {weather['sunset']}")

    await callback.message.answer(text=response,reply_markup=sozlamalar)

@dp.callback_query(F.data=="kunlik")
async def orqaga(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    data = await state.get_data()
    city_name = data.get("city_name")
    forecast_output = get_weather_forecast(city_name)
    await callback.message.answer(forecast_output, reply_markup=sozlamalar)

@dp.callback_query(F.data=="sozlamalar")
async def sozlama(callback:CallbackQuery, state: FSMContext):
    await callback.message.delete()
    data = await state.get_data()
    city_name = data.get("city_name")
    await callback.answer("Sozlamalar")
    text = f"Hozirgi sozlamalaringiz:\n\n📍Shahar: {city_name}"
    await callback.message.answer(text, reply_markup=sozlamalarni_ichi)

@dp.callback_query(F.data=="ortga")
async def orqaga(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Qanday Ob-havo malumotlarini olishni istaysiz!", reply_markup=sozlamalar)



@dp.callback_query(F.data=="shahar")
async def havo(callback:CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Qanday Ob-havo malumotlarini olishni istaysiz!", reply_markup=weather_inl_button)

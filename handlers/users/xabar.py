# from aiogram.types import Message
# from loader import dp, bot, ADMINS
# from aiogram import F
# from aiogram.filters import Command, CommandStart, or_f
# from states.help_stt import Help
# from states.reklama import Adverts, AdminMSG
# from aiogram.fsm.context import FSMContext



# # @dp.message(or_f(Command("xabar"), (F.text == "👤Admin bilan bog'lanish")))
# # async def help_commands(message:Message,state:FSMContext):
# #     await message.answer("Xabaringizni yozib qoldiring✍🏻 \nMurojatingiz 👤 adminga boradi!")

# #     await state.set_state(AdminMSG.msg)

# # @dp.message(Help.help)
# # async def send_advert(message:Message,state:FSMContext):
# #     msg = message.text
# #     await message.answer("Sizning xabaringiz 👤adminga bordi✅\n👤Admin albatta javob yozadi!")
# #     text = f"📬<b>ob-havo Bot dan murojat keldi! \n</b>👤<b>Foydalanuvchi:</b>➡️ @{message.from_user.username}\n📜<b>Xabar</b>: {msg}"
# #     for admin in ADMINS:
# #         await bot.send_message(chat_id=admin, text=text, parse_mode='html')
# #     await state.clear()
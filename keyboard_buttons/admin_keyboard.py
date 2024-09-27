from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

admin_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍💼Admin"),        
        ]      
    ],
  resize_keyboard=True
)

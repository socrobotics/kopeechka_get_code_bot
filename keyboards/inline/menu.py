from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Код отправлен"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_after = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_end = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Получить еще один код"),
        ]
    ],
    resize_keyboard=True
)

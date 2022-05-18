from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.menu import menu_end
from loader import dp


@dp.message_handler(Text(contains="Завершить работу"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вы завершили работу\n"
                         f"До новых встреч!✋", reply_markup=menu_end)


@dp.message_handler(Text(contains="Получить еще один код"))
async def close_app(message: types.Message):
    await message.answer(f"Я перезапустился\n"
                         f"Отправь мне email, на который хочешь получить код\n"
                         f"До новых встреч!✋", reply_markup=types.ReplyKeyboardRemove())

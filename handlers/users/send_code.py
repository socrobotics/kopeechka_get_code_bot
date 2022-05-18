from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp

from keyboards.inline.menu import menu_after


@dp.message_handler(Text(contains="Код отправлен"))
async def get_code(message: types.Message):
    await message.answer("Ожидаю код...", reply_markup=menu_after)

    # code = get_code()


@dp.message_handler(Text(contains="Завершить работу"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вы завершили работу\n"
                         f"До новых встреч!✋", reply_markup=types.ReplyKeyboardRemove())
from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.menu import menu_after
from loader import dp


@dp.message_handler(Text(contains="Код отправлен"))
async def get_code(message: types.Message):
    await message.answer("Ожидаю код...", reply_markup=menu_after)

    # code = get_code()
    # if code != "":
    #     await message.answer(f"Код получен - {code}", reply_markup=menu_end)
    # else:
    #     await message.answer("Не удалось получить код, жми 👇 Получить код еще раз 👇 ", reply_markup=menu_again)

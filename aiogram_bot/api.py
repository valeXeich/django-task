import aiohttp
from aiogram import types


async def create_user(data: dict, message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.post('https://django-backend-production.up.railway.app/sign-up', json=data) as resp:
            response = await resp.json()
            if resp.status == 400:
                msg = response.get('message')
                email = response.get('email')
                await message.answer(f'{msg}\nВаш email: {email}')
            else:
                msg = response.get('message')
                password = data.get('password')
                email = data.get('email')
                await message.answer(f'{msg}\nВаш email: {email}\nВаш пароль: {password}')
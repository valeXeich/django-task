from aiogram.utils import executor

from bot import dp
from handlers import sign_up


async def on_startup(_):
    print('Bot online')


sign_up.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
import os
import asyncio

from aiogram import Bot, Dispatcher

from bot import start



async def main():
     bot = Bot(os.environ.get('TOKEN'))
     dp = Dispatcher()
     
     dp.include_routers(
          start.start_router
     )
     await dp.start_polling(bot)
     
     
if __name__ == '__main__':
     asyncio.run(main())
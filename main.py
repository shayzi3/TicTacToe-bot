import os
import asyncio

from aiogram import Bot, Dispatcher

from bot import start, echo



async def main():
     bot = Bot(os.environ.get('TOKEN'))
     dp = Dispatcher()
     
     dp.include_routers(
          start.start_router,
          echo.echo_router
     )
     await dp.start_polling(bot)
     
     
if __name__ == '__main__':
     asyncio.run(main())
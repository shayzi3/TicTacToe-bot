import os
import asyncio

from loguru import logger
from aiogram import Bot, Dispatcher

from handlers import start, echo, callback
from models import function_main



async def main():
     function_main() # Пересоздаёт json файл
     
     bot = Bot(os.environ.get('TOKEN'))
     dp = Dispatcher()
     
     dp.include_routers(
          start.start_router,
          echo.echo_router,
          callback.callback_router
     )
     
     async with bot as update:
          await update.get_updates(request_timeout=3)
            
     logger.info("BOT STARTED SUCCESS...")
     await dp.start_polling(bot)
     
     
     
if __name__ == '__main__':
     asyncio.run(main())
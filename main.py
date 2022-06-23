import asyncio

from sys import exit
from os import getenv
from loguru import logger
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types

from bot.handlers.bot_commands import register_bot_commands
from bot.handlers.bot_messages import register_bot_messages


def register_all_handlers(dp):
    register_bot_commands(dp)
    register_bot_messages(dp)


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start bot"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logger.add("logs/bot.log", level="INFO", encoding="utf8",
               format='{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level: <8}</level> | {name}:{function}:{line} - '
                      '<level>{''message}</level>',
               filter=None, colorize=None, backtrace=True, diagnose=True, enqueue=False, catch=True,
               rotation="1 days", compression="zip")

    logger.add("logs/error.log", level="ERROR", encoding="utf8",
               format='{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level: <8}</level> | {name}:{function}:{line} - '
                      '<level>{''message}</level>',
               filter=None, colorize=None, backtrace=True, diagnose=True, enqueue=False, catch=True,
               rotation="1 days", compression="zip")

    bot_token = getenv("BOT_TOKEN")
    if not bot_token:
        logger.error('Error: no Bot token provided')
        exit("Error: no Bot token provided")

    bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    await set_bot_commands(bot)

    logger.info('Starting bot..')

    try:
        await dp.start_polling()
    finally:
        session = await bot.get_session()
        await session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")

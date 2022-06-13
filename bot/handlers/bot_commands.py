from aiogram import types, Dispatcher
from loguru import logger

from bot.config import bot_version


async def cmd_start(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <start>')
    await message.answer(f"Hello {message.from_user.username}")


async def cmd_version(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <version>')
    await message.answer(f"Bot version: <b>{bot_version}</b>")


async def cmd_id(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <ID>')
    await message.answer(f"Your ID: <b>{message.from_user.id}</b>")


def register_bot_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_version, commands=["version"])
    dp.register_message_handler(cmd_id, commands=["id"])

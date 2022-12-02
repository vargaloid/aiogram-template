from aiogram import types, Dispatcher
from loguru import logger

from bot.handlers.user import UserManagement
from bot.keyboards.inline import inline_kb_users
from bot.misc.user import get_users
from config import debug_mode


async def cmd_start(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <start>')
    if debug_mode:
        logger.debug(f'Command: <start> - {message}')
    await message.answer(f"Hello {message.from_user.username}")


async def cmd_user(message: types.Message):
    logger.info(f'Command: <user> - {message.from_user.username}:{message.from_user.id}')
    users = get_users()
    msg = "<b>Users list:</b>"
    for user_id in users.keys():
        msg_user = f'{user_id} - {users.get(user_id)}'
        msg = msg + '\n' + msg_user
    await message.answer(msg, reply_markup=inline_kb_users)
    await UserManagement.waiting_add_or_del.set()


async def cmd_version(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <version>')
    if debug_mode:
        logger.debug(f'Command: <version> - {message}')
    await message.answer(f"Bot version: <b>0.0.0</b>")


async def cmd_id(message: types.Message):
    logger.info(f'{message.from_user.username}:{message.from_user.id} - command: <ID>')
    if debug_mode:
        logger.debug(f'Command: <ID> - {message}')
    await message.answer(f"Your ID: <b>{message.from_user.id}</b>")


def register_bot_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"], state='*', is_user=True)
    dp.register_message_handler(cmd_user, commands=["user"], state='*', is_user=True)
    dp.register_message_handler(cmd_version, commands=["version"], state='*', is_user=True)
    dp.register_message_handler(cmd_id, commands=["id"], state='*',
                                chat_type=['private', 'supergroup', 'group'],
                                is_user=True)

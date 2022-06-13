from aiogram import types, Dispatcher
from loguru import logger


# async def bot_reply_msg(message: types.Message):
#     await message.reply("reply")


async def bot_answer_msg(message: types.Message):
    await message.answer("answer")


def register_bot_messages(dp: Dispatcher):
    # dp.register_message_handler(bot_reply_msg)
    dp.register_message_handler(bot_answer_msg)

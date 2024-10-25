import logging

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.fsm.storage.redis import RedisStorage
from aiogram_dialog import setup_dialogs

from bot.commands import register_commands
from bot.dialogs import register_dialogs
from service.config.config_structure import Config


async def start_bot(config: Config):
    """Start the bot"""
    logging.info("Bot starting")
    storage = RedisStorage.from_url(url=config.redis.get_connection_url(), key_builder=DefaultKeyBuilder(with_destiny=True))

    dp = Dispatcher(
        events_isolation=SimpleEventIsolation(),
        storage=storage
    )
    bot = Bot(config.bot.api_token)

    await register_dialogs(dp)
    setup_dialogs(dp)
    register_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем апдейты
    await dp.start_polling(bot)  # Запускам пуллинг бота

from aiogram import Dispatcher, F
from aiogram.filters import Command

from bot.commands.start import start

def register_commands(dp: Dispatcher):
    dp.message.register(start, Command(commands=['start']))
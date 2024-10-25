from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs.main_dialog.main_menu import states


async def interactive(c: CallbackQuery, widget: Button, manager: DialogManager):
    # await manager.switch_to(states.MainMessage.main_message)
    await c.answer("Заглушка")


async def settings(c: CallbackQuery, widget: Button, manager: DialogManager):
    # await manager.switch_to(states.MainMessage.main_message)
    await c.answer("Заглушка")


async def information(c: CallbackQuery, widget: Button, manager: DialogManager):
    # await manager.switch_to(states.MainMessage.main_message)
    await c.answer("Заглушка")


async def forward(c: CallbackQuery, widget: Button, manager: DialogManager):
    # await manager.switch_to(states.MainMessage.main_message)
    await c.answer("Заглушка")

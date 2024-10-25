from aiogram import Dispatcher

from bot.dialogs import main_dialog

async def register_dialogs(dp: Dispatcher):

    for dialog in [
        *await main_dialog.main_menu_dialogs(),
    ]:

        dp.include_router(dialog)
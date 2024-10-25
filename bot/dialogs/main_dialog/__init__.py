from aiogram_dialog import Dialog

from bot.dialogs.main_dialog.main_menu import windows as main_menu_windows

async def main_menu_dialogs():
    return [
        Dialog(
            await main_menu_windows.main_message(),
        )
    ]
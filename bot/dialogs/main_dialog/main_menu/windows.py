from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.main_dialog.main_menu import (
selecters, states, keyboards, getters
)


async def main_message():
    return Window(
        Format("Приветствую, товарищь {user_name}"),
        keyboards.main_message(
            interactive=selecters.interactive,
            settings=selecters.settings,
            information=selecters.information,
            forward=selecters.forward
        ),
        getter=getters.main_message,
        state=states.MainMessage.main_message
    )
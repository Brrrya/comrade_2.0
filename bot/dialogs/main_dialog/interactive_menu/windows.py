from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.main_dialog.interactive_menu import (
selecters, states, keyboards, getters
)


async def interactive_message():
    return Window(
        Const("Интерактивное меню"),
        keyboards.interactive_message(
            create_call=selecters.create_call,
            feedback=selecters.feedback,
        ),
        Cancel(Const("Главное меню")),
        getter=getters.interactive_message,
        state=states.InteractiveMeny.interactive_menu
    )
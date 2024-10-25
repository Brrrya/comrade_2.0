from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.main_dialog.main_menu.states import MainMessage



async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMessage.main_message, mode=StartMode.RESET_STACK,
                               data={"user_name": message.from_user.first_name}
                               )
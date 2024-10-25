from aiogram_dialog import DialogManager


async def main_message(dialog_manager: DialogManager, **kwargs):
    return {"user_name": dialog_manager.start_data.get("user_name")}
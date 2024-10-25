
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Const


def interactive_message(
        create_call,
        feedback
):
    return Group(
        Button(Const("Создать созвон"), on_click=create_call, id='create_call'),
        Button(Const("Обратная связь/Баг репорт"), on_click=feedback, id='feedback')
    )
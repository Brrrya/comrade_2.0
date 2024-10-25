from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Const


def main_message(
        interactive, settings, information, forward
):
    return Group(
        Button(Const("Интерактив"), on_click=interactive, id="interactive_button"),
        Button(Const("Настройки"), on_click=settings, id="settings_button"),
        Button(Const("Данные по запросу"), on_click=information, id="information_button"),
        Button(Const("Пересылка сообщений из RocketChat"), on_click=forward, id="forward_button"),
    )
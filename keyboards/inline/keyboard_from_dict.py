from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import urllib
import re


def keyboard_from_dict(dictionary: dict):
    keyboard = InlineKeyboardMarkup()
    buttons: list[InlineKeyboardButton] = []
    for k, v in dictionary.items():
        if v.startswith("https://fm"):
            btn = InlineKeyboardButton(k, url=v)
            buttons.append(btn)
            # keyboard.add(btn, row_width=2)
        else:
            btn = InlineKeyboardButton(k, callback_data=v)
            buttons.append(btn)
    keyboard.add(*buttons, row_width=2)

    return keyboard


if __name__ == "__main__":
    print("Отменавсам".split("Отмена"))

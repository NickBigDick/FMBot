from telebot.types import Message, CallbackQuery
from states.UserState import UserState
from loader import bot
from handlers.default_heandlers.auth import authorization, get_user_fmid
from fmapi.Families import Family
from keyboards.inline.keyboard_from_dict import keyboard_from_dict


@bot.message_handler(commands=['find_family_by_id'])
def family_name(message: Message):
    if authorization(message):
        bot.send_message(message.chat.id, "Введите id семейства")
        bot.set_state(message.from_user.id, UserState.find_family_by_id, message.chat.id)


@bot.message_handler(state=UserState.find_family_by_id)
def request(message: Message):
    user_id = get_user_fmid(message.from_user.username)
    if user_id:
        family_url = Family(family_id=message.text).url
        if family_url:
            d = {message.text: family_url}
            keyboard = keyboard_from_dict(d)
            bot.send_message(message.chat.id, "Семейство: ", reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, "К сожалению семейство я не нашел")
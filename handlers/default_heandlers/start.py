from telebot.types import Message

from handlers.default_heandlers.auth import authorization
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    if authorization(message):
        bot.reply_to(message, f"Привет, {message.from_user.full_name} \n"
                              f"Вы авторизованы")
    else:
        bot.reply_to(message, f"Привет, {message.from_user.full_name} \n"
                              f"Необходимо авторизоваться. Введите адрес вашей электронной почты. Пример: example@pik.ru")


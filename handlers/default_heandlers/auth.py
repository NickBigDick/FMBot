from database.model import *
from fmapi.Users import User
from telebot.types import Message, CallbackQuery
from loader import bot
from states.UserState import UserState


def check_auth_table():
    with db:
        tables = db.get_tables()
        model_tables = {'users': UserData}
        for model_table in model_tables.keys():
            if model_table not in tables:
                db.create_tables([model_tables[model_table]])
    return True


def get_user_fmid(telegram_username: str):
    if UserData.select().where(UserData.telegram_username == telegram_username):
        for user in UserData.select().where(UserData.telegram_username == telegram_username):
            return user.fm_id


def add_user(telegram_username: str, fm_username: str, fm_email: str, fm_id: int, chat_id: int, telegram_user_id:int):
    UserData.create(telegram_username=telegram_username, fm_username=fm_username, fm_email=fm_email, fm_id=fm_id,
                    chat_id=chat_id, telegram_user_id=telegram_user_id)


def authorization(message: Message):
    """

    Авторизация пользователя

    :param message:
    :return:
    """
    if get_user_fmid(message.from_user.username):
        return True
    else:
        bot.send_message(message.chat.id, "Необходимо авторизоваться. Используйте команду /start")


@bot.message_handler(regexp="@pik.ru")
def login(message: Message):
    """

    Регистрация пользователя

    :param message:
    :return:
    """
    user = User(message.text).get_user()
    if user:
        user_info = user
        add_user(telegram_username=message.from_user.username, fm_username=user_info['name'],
                 fm_email=user_info['login'],
                 fm_id=user_info['id'],
                 chat_id=message.chat.id,
                 telegram_user_id=message.from_user.id)
        bot.send_message(message.chat.id, "Поздравляем с авторизацией")
        pass
    else:
        bot.send_message(message.chat.id, "Учетная запись не найдена")


if __name__ == "__main__":
    if check_auth_table():
        # if get_user_fmid("irina_rrrrrt"):
        #     print("dd")
        # else:
        #     add_user("irina_rrrrrt", "Рыжкова И. И.", "оо", 13736)
        #     print(get_user_fmid("Niko0707"))
        authorization("Niklo0707")
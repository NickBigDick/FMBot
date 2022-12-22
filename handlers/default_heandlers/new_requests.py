import re

from telebot.types import Message, CallbackQuery

from handlers.default_heandlers.auth import authorization
from keyboards.inline.keyboard_from_dict import keyboard_from_dict
from loader import bot
from states.UserState import UserState
from fmapi import Requests, RequestStatuses
from fmapi.Disciplines import Disciplines

requests_collections = {
  "АР/АИ/TX": f"{Disciplines().AR} {Disciplines().AI} {Disciplines().TX}",
  "КР/КМ/КЖС": f"{Disciplines().KR} {Disciplines().KM} {Disciplines().KJC}",
  "ОВ/ВК/ТМ": f"{Disciplines().OV} {Disciplines().VK} {Disciplines().TM}",

}

#обработка начальной команды
@bot.message_handler(commands=['new_requests'])
def func(message: Message):
    if authorization(message):
        keyboard = keyboard_from_dict(requests_collections)
        bot.send_message(message.chat.id, "Выберите дисциплины:", reply_markup=keyboard)
        bot.set_state(message.from_user.id, UserState.new_requests, message.chat.id)


#обработка кноки "Отмена", возвращающей к заявкам
@bot.callback_query_handler(func=lambda call: "Заявки" in call.data)
def call_back_cancellation(callback: CallbackQuery):
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        d = data["Заявки"]
    keyboard = keyboard_from_dict(d)
    bot.edit_message_text(f'Заявки: ', chat_id=callback.message.chat.id,
                          message_id=callback.message.id, reply_markup=keyboard)


#обработка кноки "Отмена", возвращающей к Главному меню
@bot.callback_query_handler(func=lambda call: "Главное меню" in call.data)
def call_back_cancellation(callback: CallbackQuery):
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        d = data["Главное меню"]
    keyboard = keyboard_from_dict(d)
    bot.edit_message_text(f'Какие заявки Вам интересны?', chat_id=callback.message.chat.id,
                          message_id=callback.message.id, reply_markup=keyboard)


#Обработка списка заявок
@bot.callback_query_handler(func=lambda call: "пояснение к заявке " in call.data)
def call_back_description(callback: CallbackQuery):
    id = int(re.findall("\d+", callback.data)[0])
    request = Requests.Request(id).get_request()
    description = f"Заявка {id}\n" + request["description"] + f"\nСсылка на заявку: {Requests.Request(id).url}"
    bot.edit_message_text(text=description, chat_id=callback.message.chat.id,
                          message_id=callback.message.id)


@bot.callback_query_handler(func=None, state=UserState.new_requests)
def call_back(callback: CallbackQuery):
    discipline_ids = [int(string) for string in callback.data.split()]

    file = Requests.post_requests_filter(requeststatuses=[
        RequestStatuses.RequestStatus().moderation,
        RequestStatuses.RequestStatus().appointment_executor
    ],
        disciplineids=discipline_ids)
    d = {}
    for r in file:
        short_info = str(r['id']) + ", Инициатор: " + r['initiator']['name'] + ", ФТ: " + r["functionalType"][
            "name"]
        request = Requests.Request(r['id'])
        d[f"Пояснение {str(r['id'])}"] = "пояснение к заявке " + str(r['id'])
        d[short_info] = request.url
    d["Отмена"] = "Главное меню"

    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data["Заявки"] = d
        data["Главное меню"] = requests_collections
    keyboard = keyboard_from_dict(d)
    bot.edit_message_text(f'Заявки: ', chat_id=callback.message.chat.id,
                          message_id=callback.message.id, reply_markup=keyboard)


import re

from telebot.types import Message, CallbackQuery
from states.UserState import UserState
from loader import bot
from keyboards.inline.keyboard_from_dict import keyboard_from_dict
from fmapi import Requests, RequestStatuses
from handlers.default_heandlers.auth import authorization, get_user_fmid

requests_types = {
    "Заполнение заявки": "writing_request",
    "Модерация": "moderation",
    "Согласование заявки": "coordination",
    "Назначение исполнителя": "appointment_executor",
    "Исполнение заявки": "inprogress",
    "Проверка решения модератором": "moderator_check",
    "Проверка решения инициатором": "initiator_check",
    "Заявка выполнена": "ready",
    "Заявка отменена": "canceled"
}

#обработка начальной команды
@bot.message_handler(commands=['my_requests'])
def request_type(message: Message):
    if authorization(message):
        keyboard = keyboard_from_dict(requests_types)
        bot.send_message(message.chat.id, "Какие заявки Вам интересны?", reply_markup=keyboard)
        bot.set_state(message.from_user.id, UserState.my_requests, message.chat.id)


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
    id = int(re.findall('\d+', callback.data)[0])
    request = Requests.Request(id).get_request()
    description = f"Заявка {id}\n" + request["description"] + f"\nСсылка на заявку: {Requests.Request(id).url}"
    d = {"Отмена": "Заявки"}
    keyboard = keyboard_from_dict(d)
    bot.edit_message_text(text=description, chat_id=callback.message.chat.id,
                          message_id=callback.message.id, reply_markup=keyboard)


#Обработка
@bot.callback_query_handler(func=None, state=UserState.my_requests)
def call_back(callback: CallbackQuery):
    user_id = get_user_fmid(callback.from_user.username)
    if user_id:
        file = Requests.post_requests_filter(userrelatedid=user_id, requeststatuses=[RequestStatuses.RequestStatus().
                                             get_requeststatus_by_string(callback.data)])
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
            data["Главное меню"] = requests_types
        keyboard = keyboard_from_dict(d)
        bot.edit_message_text(f'Заявки: ', chat_id=callback.message.chat.id,
                              message_id=callback.message.id, reply_markup=keyboard)

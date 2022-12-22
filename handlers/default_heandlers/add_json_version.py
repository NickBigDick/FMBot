import requests
from telebot.types import Message, CallbackQuery

from biminspectorapi.PlacementModule import PlacementModule
from states.UserState import UserState
from loader import bot
from handlers.default_heandlers.auth import authorization, get_user_fmid
from fmapi.Families import Family
from fmapi.Versions import Version
from keyboards.inline.keyboard_from_dict import keyboard_from_dict


@bot.message_handler(commands=['add_json_version'])
def family_name(message: Message):
    if authorization(message):
        bot.send_message(message.chat.id, "Введите имя семейства")
        bot.set_state(message.from_user.id, UserState.add_json_version, message.chat.id)


@bot.message_handler(state=UserState.add_json_version)
def request(message: Message):
    user_id = get_user_fmid(message.from_user.username)
    if user_id:
        family_names = message.text.split("\n")
        for family_name in family_names:
            family = Family(family_name=family_name)
            print(family.FMId)
            if family.FMId:
                lastVersion = family.lastversionid
                if lastVersion:
                    code = PlacementModule(family_name).get_modulejson()
                    if code:
                        path = f"Jsons/{family_name}.json"
                        attachements = Version(lastVersion).get_attachements()
                        if attachements:
                            for attachement in attachements:
                                id = attachement['id']
                                if id:
                                    Version(lastVersion).delete_attachement(id)
                                    print(f"Удалено вложение {family_name}")
                        version = Version(lastVersion).post_file_to_version(path)
                        print(f"Добавлено вложение {family_name}")

                        d = {family_name: family.url}
                        keyboard = keyboard_from_dict(d)
                        bot.send_message(message.chat.id, "Возникает ощущение, что на работу встаем чаще, чем ложимся спать.\nВерсия семейства успешно обновила json: ", reply_markup=keyboard)
                    else:
                        bot.send_message(message.chat.id, f"К сожалению я не смог скачать json {family_name}")
            else:
                bot.send_message(message.chat.id, "К сожалению семейство я не нашел")
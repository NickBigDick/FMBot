from telebot.types import Message


from states.UserState import UserState
from loader import bot

from handlers.default_heandlers.auth import authorization
from fmapi.Requests import Request
from utils.request_to_api import send_request_to_api


def put_basic_moderator_attributes(request_id, example_request_id=40777, file=None):
    try:
        example_request = Request(example_request_id).get_request()
        example_attributes = example_request["moderatorAttributes"]
        file = Request(request_id).get_request()

        file["disciplines"][0] = file["disciplines"][0]["id"]
        file["functionalType"] = file["functionalType"]["id"]

        initiatorattributes = []
        for dic in file["initiatorAttributes"]:
            if dic["options"]:
                if type(dic["options"][0]) == dict:
                    new_opt = [attr["id"] for attr in dic["options"]]
            else:
                new_opt = dic["options"]
            new_dic = {
                "id": dic["id"],
                "attributeId": dic["attributeId"],
                "ownerId": dic["ownerId"],
                "valueStr": dic["valueStr"],
                "options": new_opt,
                "isDeleted": 1,
                "isValueUpdated": 0
            }
            initiatorattributes.append(new_dic)
        file["initiatorAttributes"] = initiatorattributes

        moderator_attributes = [i for i in file["moderatorAttributes"]]
        for i in example_attributes:
            if i["options"] and type(i["options"][0]) == dict:
                new_opt = [attr["id"] for attr in i["options"]]
            else:
                new_opt = i["options"]
            new_d = {
                "id": i["id"],
                "attributeId": i["attributeId"],
                "ownerId": file["id"],
                "valueStr": i["valueStr"],
                "options": new_opt,
                "isDeleted": 1,
                "isValueUpdated": 0
            }
            moderator_attributes.append(new_d)
        file["moderatorAttributes"] = moderator_attributes
        print("атрибуты присвоены")
        # response = requests.request("PUT", 'https://fm-api.bimteam.ru/v1/Requests/{}'.format(str(request_id)),
        #                             headers=headers, json=file)
        # if response.status_code == 200:
        #     print("Атрибуты присвоены")

        response = send_request_to_api('https://fm-api.bimteam.ru/v1/Requests/{}'.format(str(request_id)), jsonn=file,
                                       method="PUT")
        if response.status_code == 200:
            return response
    except:
        print(f"Ошибка назначения атрибутов модератора {request_id}")


if __name__ == "__main__":
    put_basic_moderator_attributes(41693)


@bot.message_handler(commands=['basic_moderator_attributes'])
def request_type(message: Message):
    if authorization(message):
        bot.reply_to(message, "Напишите номер заявки")
        bot.set_state(message.from_user.id, UserState.set_moderator_attributes, message.chat.id)


@bot.message_handler(state=UserState.set_moderator_attributes, is_digit=True)
def put_moderator_attributes(message: Message):
    if put_basic_moderator_attributes(message.text):
        bot.send_message(message.chat.id, "Атрибуты заявке успешно присвоены")
    else:
        bot.send_message(message.chat.id, "Ошибка присвоения атрибутов")


@bot.message_handler(state=UserState.set_moderator_attributes, is_digit=False)
def number_incorrect(message: Message):
    bot.send_message(message.chat.id, "Похоже, что Вы ввели не номер заявки. Попытайтесь снова")



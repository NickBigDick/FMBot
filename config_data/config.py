import json
import os
from os import path
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('my_requests', "Показать мои заявки"),
    ('basic_moderator_attributes', "Установить базовые атрибуты модератора заявке"),
    ('new_requests', "Показать новые заявки"),
    ("find_family", "Найти семейство"),
    ("find_family_by_id", "Найти семейство по id"),
    ("find_family_by_versionid", "Найти семейство по id версии семейства"),
    ("add_json_version", "Добавить/Обновить json модуля")
)

FM_PATH = os.getenv('PATH_TO_FM_CODE')
token_path = path.abspath(FM_PATH) # noqa


def update_token():

    with open(token_path, "r") as f:
        file = json.load(f)
        token = file["access_token"]
        return token


def create_headers():
    headers = {
        'FmClientType': 'fm-webapp',
        'Authorization': 'Bearer ' + update_token()
    }
    return headers

def create_headers_json():
    headers_json = {
        'FmClientType': 'fm-webapp',
        'Authorization': 'Bearer ' + update_token(),
        'Content-Type': 'application/json; charset=utf-8'
    }
    return headers_json


from email import header
import json
import requests
from os import path
from config_data.config import headers


def get_families_by_family_type_name(search):

    query = {
        'SearchString': search
    }

    response = requests.request("GET", "https://fm-api.bimteam.ru/v1/FamilySymbols/search", headers=headers,
                                params=query)
    file = json.loads(response.text)
    file_path = path.abspath(r'FM\log.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json_file = json.dumps(file, ensure_ascii=False, indent=4)
        f.write(json_file)
    return file


def get_familysymbols_smartsearch(search) -> list:

    """

    Триграммный поиск по имени

    :param search: подстрока поиска в имени типоразмера
    :return: list
    """
    query = {
        'SearchString': search,

    }

    response = requests.request('GET', "https://fm-api.bimteam.ru/v1/FamilySymbols/smartSearch", headers=headers,
                                params=query)
    file = json.loads(response.text)
    return file


def get_familysymbols_id(familysymbol_id: str) -> dict:
    """

    возвращает объект по ID

    :param familysymbol_id:
    :return:
    """
    response = requests.request("GET", f"https://fm-api.bimteam.ru/v1/FamilySymbols/{familysymbol_id}",
                                headers=headers)
    file = json.loads(response.text)
    return file


def fmid_from_familysymbol(dic: dict) -> str:

    """

    Возвращает FMId семейства, которому принадлежит типоразмер

    dic: словарь с информацией о типоразмере
    return: возвращает FMId
    """
    fmid_parameter_id = 10547
    for d in dic["parameterValueSets"][0]["parameterValues"]:
        if d['parameterId'] == fmid_parameter_id:
            fmid = d['valueStr']
            return fmid

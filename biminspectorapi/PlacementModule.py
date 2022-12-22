import json
import os

from utils.request_to_api_biminspector import send_request_to_api
import requests
from config_data.config_biminspector import headers_json
class PlacementModule:
    """

    Класс модуля
    """
    def __init__(self, modulename):
        """

        :param modulename: имя модуля
        """
        self.modulename = modulename
        dType = {
            "KV": [6, 5010],
            #"KV": [6, 5012],
            "VK": [8, 5010],
            #"OV": [9, 5011]
            "OV": [9, 5010]
        }

        self.moduletype = dType[modulename[:2]][0]
        self.port = dType[modulename[:2]][1]

    def get_modulejson(self):
        """

        Возвращает json модуля
        """

        response = requests.request('GET',
                                    f"https://vpp-bimins01.main.picompany.ru:{self.port}/BI/v2/PlacementModule/name/{self.modulename}?dataSourceType={self.moduletype}",
                                    verify=False)
        if response.status_code == 200:
            data = response.json()
            with open(f'Jsons/{self.modulename}.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return response.json()
        else:
            print(f"{self.modulename} возникла ошибка {response.status_code}")
            return None

if __name__ == "__main__":
    dir_path = r"C:\Users\tevosiannkh\Desktop\Модули\52_ВК"
    for adress, dirs, files in os.walk(dir_path):
        for file in files:
            if file.find("SHD") == -1 and file.find("00") == -1 and file.endswith("rvt"):
                full_path = adress + '\\' + file
                PlacementModule(file[:-4]).get_modulejson()

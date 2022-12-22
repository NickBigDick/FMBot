import json

import requests

from utils.request_to_api import send_request_to_api


class Version:
    """

    Класс семейства Revit
    """

    def __init__(self, versionid=None):
        """

        :param fmid: FMID
        :param familyid: id семейства
        """
        self.versionid = versionid


    def get_version(self) -> dict:
        """

        Возвращает версию семейства
        """

        response = send_request_to_api('https://fm-api.bimteam.ru/v1/Versions/{}'.format(str(self.versionid)))
        file = json.loads(response.text)
        return file

    def get_attachements(self):
        """
        Возвращает json вложение
        """

        response = send_request_to_api("https://fm-api.bimteam.ru/v1/Versions/attachments/", jsonn=[self.versionid])
        file = json.loads(response.text)
        return file

    def delete_attachement(self, attachementid):
        """
        Удаляет вложение

        """
        url = f"https://fm-api.bimteam.ru/v1/Versions/{str(self.versionid)}/attachments/{str(attachementid)}"
        response = send_request_to_api(url, method="DELETE")
        return response.status_code

    def get_version_status_id(self, check_actual=False):
        """

        Возвращает статус версии семейства
        Если check_actual = True, вернет актуальна ли версия
        1: Разрешена
        2: На проверке
        3: Запрещен
        4: Устарела
        """
        if check_actual:
            return self.get_version()['familyVersionStatusId'] == 1
        else:
            return self.get_version()['familyVersionStatusId']

    def post_file_to_version(self, path):
        url = f'https://fm-api.bimteam.ru/v1/Versions/{self.versionid}/attachments'

        with open(path, 'rb') as f:
            #files = {'files': ('OV2.V_KV_DD_STK_3.6_ST_0NS_(6.3)R01_3.6x6.3_A_V0_(N)_(N)_none.json', f.read())}
            files = {'files': (f.name.split('/')[-1], f.read())}
            #r = requests.post(url, headers=headers, files=files)
            response = send_request_to_api(url, files=files)
            return response

    @property
    def url(self):
        if self.versionid:
            vers = self.get_version()
            familyid = vers["familyId"]
            ft_id = vers["family"]["functionalTypeId"]
            version = vers["version"]
            #"https://fm.bimteam.ru/families/177623;functionalTypeId=1058;version=2"
            return f"https://fm.bimteam.ru/families/{familyid};functionalTypeId={ft_id};version={version}"

if __name__ == "__main__":
    pass
    # version = Version(10225).get_version()
    # print(version["family"]["functionalTypeId"])
    # print(version["family"]["name"])


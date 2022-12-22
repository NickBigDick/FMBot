import json
from utils.request_to_api import send_request_to_api


class Folder:
    """

    Класс функционального типа Revit
    """

    def __init__(self, folderid=None):
        """

        :param folderid: folderid
        """
        self.folderid = folderid

    def get_folderid(self) -> dict:
        """

        Возвращает версию семейства
        """

        response = send_request_to_api('https://fm-api.bimteam.ru/v1/Folders/{}'.format(str(self.folderid)))
        file = json.loads(response.text)
        return file


if __name__ == "__main__":
    version = Folder(82755).get_folderid()
    print(version["discipline"]["name"])
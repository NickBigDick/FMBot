import json
from utils.request_to_api import send_request_to_api


class FunctionalType:
    """

    Класс семейства Revit
    """

    def __init__(self, functionaltypeid=None):
        """

        :param functionaltypeid: functionaltypeid
        """
        self.functionaltypeid = functionaltypeid

    def get_functionaltypeid(self) -> dict:
        """

        Возвращает версию семейства
        """

        response = send_request_to_api('https://fm-api.bimteam.ru/v1/FunctionalTypes/{}'.format(str(self.functionaltypeid)))
        file = json.loads(response.text)
        return file


if __name__ == "__main__":

    functionaltype = FunctionalType(545).get_functionaltypeid()
    print(functionaltype["disciplines"])
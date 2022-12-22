import json
from pprint import pprint

from utils.request_to_api import send_request_to_api
from fmapi.Users import User


class Request:

    def __init__(self, request_id: int):
        """

        :param request_id: номер заявки
        """
        self.request_id = request_id

    def get_request(self):
        response = send_request_to_api('https://fm-api.bimteam.ru/v1/Requests/{}'.format(str(self.request_id)))
        file = json.loads(response.text)
        return file

    @property
    def url(self):
        return f"https://fm.bimteam.ru/requests/{self.request_id}"


def post_requests_filter(initiator=None, moderator=None, approver=None, developer=None,
                         requeststatuses: list = None, userrelatedid: int = None, disciplineids: list = None) -> dict:
    """

    Возвращает информацию по заявкам от пользователя

    :param initiator: Фамилия И. О. инициатора
    :param moderator: Фамилия И. О. модератора
    :param approver: Фамилия И. О. согласующего
    :param developer: Фамилия И. О. разработчика
    :param requeststatuses: RequestsStatuses statusid
    :param userrelatedid: пользователь от которого зависит заявка
    :param disciplineids: id дисциплин

    :return:
    """
    body = {
        "initiator": initiator,
        "moderator": moderator,
        "approver": approver,
        "developer": developer,
        "requestStatuses": requeststatuses,
        "userRelatedId": userrelatedid,
        "disciplineIds": disciplineids
    }

    json_body = json.dumps(body, indent=4)
    response = send_request_to_api('https://fm-api.bimteam.ru/v1/Requests/filter', data=json_body)
    file = json.loads(response.text)
    return file['result']


if __name__ == "__main__":
    request = Request(42384).get_request()
    pprint(request)
    # print(request.get_request())
    # print(post_requests_filter(userrelatedid=User("tevosiannkh@pik.ru").get_user_id))

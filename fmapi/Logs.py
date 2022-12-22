import json
import requests
from config_data.config import headers


def post_logs_loads_filter(fmid: int, familyversionids: int, skip=0, limit=50) -> dict:
    """

    Возвращает журнал загрузок типоразмеров версии семейства

    :param fmid: id семейства,
    :param familyversionids: id версии семейства,
    :param skip: количество записей в журнале для пропуска,
    :param limit: максимальное число записей в журнале,
    :return:
    {
      "count": 0,
      "fullCount": 0,
      "result": [
        {
          "id": 0,
          "family": {
            "id": 0,
            "name": "string"
          },
          "functionalTypes": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "familyVersionNumber": 0,
          "familyVersionStatus": {
            "id": 0,
            "name": "string"
          },
          "user": {
            "id": 0,
            "name": "string"
          },
          "document": {
            "id": 0,
            "name": "string"
          },
          "created": "2023-01-20T09:47:41.941Z",
          "familySymbols": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "familyVersionId": 0,
          "familySymbolsCount": 0,
          "documentFamilySymbolsCount": 0,
          "loadTimeSeconds": 0,
          "documentFmId": "string"
        }
      ]
    }
    """
    new_headers = headers.copy()
    new_headers['Content-Type'] = 'application/json; charset=utf-8'

    data = {
        "skip": skip,
        "limit": limit,
        "sortBy": "created",
        "sortOrder": "descending",
        "familyIds": [
            fmid
        ],
        "familyVersionIds": [
            familyversionids
        ]
    }
    json_object = json.dumps(data, indent=4)
    response = requests.request("POST", 'https://fm-api.bimteam.ru/v1/Logs/loads/filter', headers=new_headers,
                                data=json_object)
    if response.status_code == 200:
        file = json.loads(response.text)
        return file

    else:
        print(response.status_code)
        print(response.headers)


if __name__ == "__main__":
    print(post_logs_loads_filter(fmid=76242, familyversionids=212432, skip=0, limit=50))

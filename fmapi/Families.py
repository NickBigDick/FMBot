import json
import pprint

from utils.request_to_api import send_request_to_api


class Family:
    """

    Класс семейства Revit
    """

    def __init__(self, fm_id=None, family_id=None, family_name=None):
        """

        :param fm_id: FMID
        :param family_id: id семейства
        :param family_name: имя семейства

        """
        self.fm_id = fm_id
        self.family_id = family_id
        self.family_name = family_name

    def _get_family_by_familyid(self, includefunctionaltypeparameters=False) -> dict:

        """

        Возвращает семейство по Id

        :param includefunctionaltypeparameters:
        :return:
        """
        query = {
            'includeFunctionalTypeParameters': includefunctionaltypeparameters
        }

        response = send_request_to_api('https://fm-api.bimteam.ru/v1/Families/{}'.format(str(self.family_id)),
                                       params=query)
        file = json.loads(response.text)
        return file

    def _get_family_by_fmid(self) -> dict:

        """

        Возвращает семейства по FMID
        :return:
        """
        response = send_request_to_api("https://fm-api.bimteam.ru/v1/Families/fmIdsSearch", jsonn=[self.fm_id])
        file = json.loads(response.text)
        return file

    def _get_families_by_name(self) -> dict:
        """

        Возвращает семейства по имени
        :return:
        """
        response = send_request_to_api(f"https://fm-api.bimteam.ru/v1/Families/search?searchString={self.family_name}")
        file = json.loads(response.text)
        return file

    @property
    def FMId(self) -> str:
        if self.fm_id:
            d = self._get_family_by_fmid()
            if d:
                return d['result'][0]['versions'][0]['fmId']
        elif self.family_id:
            d = self._get_family_by_familyid()
            if d:
                return d["fmId"]
        elif self.family_name:
            d = self._get_families_by_name()
            for f in d:
                return f["fmId"]

    @property
    def familyid(self) -> str:
        if self.fm_id:
            d = self._get_family_by_fmid()
            if d:
                return d['result'][0]['versions'][0]['id']
        elif self.family_id:
            d = self._get_family_by_familyid()
            if d:
                return d["id"]
        elif self.family_name:
            d = self._get_families_by_name()
            if d:
                return d[0]['id']

    @property
    def familyname(self) -> str:
        """

        Возвращает имя семейства

        :return:
        """
        if self.fm_id:
            d = self._get_family_by_fmid()
            name = d['result'][1]['name']
            return name
        elif self.family_id:
            d = self._get_family_by_familyid()
            name = d["name"]
            return name

    @property
    def functionaltypename(self) -> str:
        """

        Возвращает имя функционального типа

        :return:
        """
        if self.fm_id:
            d = self._get_family_by_fmid()
            name = d['result'][0]['functionalTypes'][0]['name']
            return name
        elif self.family_id:
            d = self._get_family_by_familyid()
            name = d['functionalTypes'][0]['name']
            return name

    @property
    def functionaltypeid(self) -> str:
        """

        Возвращает id функционального типа

        :return:
        """
        if self.fm_id:
            d = self._get_family_by_fmid()
            name = d['result'][0]['functionalTypes'][0]['id']
            return name
        elif self.family_id:
            d = self._get_family_by_familyid()
            name = d['functionalTypes'][0]['id']
            return name

    @property
    def lastversionid(self) -> int:
        """

        Возвращает последнюю версию
        """
        if self.family_name:
            d = self._get_families_by_name()
            return d[0]['lastVersionId']

    @property
    def url(self):
        if self.familyid:
            return f"https://fm.bimteam.ru/families/{self.familyid}"


def post_families_filter(functionaltypeid: int, skip=0, limit=50) -> dict:
    """

    Возвращает результаты поиска по фильтру, по умолчанию первые 50 семейств

    :param functionaltypeid: id функционального типа,
    :param skip: количество записей в журнале для пропуска,
    :param limit: максимальное число записей в журнале,
    :return:

    """
    data = {
        'skip': skip,
        "limit": limit,
        "sortBy": "created",
        "sortOrder": "Ascending",
        "functionalTypeIds": [
            functionaltypeid
        ],
    }
    json_object = json.dumps(data, indent=4)
    response = send_request_to_api('https://fm-api.bimteam.ru/v1/Families/filter', data=json_object)
    result = {}
    file = json.loads(response.text)
    for i in file['result']:
        result[i['name']] = {
            'id': i['id'],
            'versionId': i['versionId']
        }
    return result


if __name__ == "__main__":
    # family = Family(fm_id='73befcfbc02a4c7e9030087b70aebcb5') # noqa
    # family = Family(family_id=172584)
    # family = Family(familyid=172584)
    family = Family(family_name="KV_Basic_BE_3.3_ST_0NL_(7.2)R04_3.3x7.235_A_V0_(N)_(N)")
    print(family.familyid)
    print(family.url)
    # print(family)
    # print(family.familyname)
    # print(family.functionaltypename)
    # print(family.functionaltypeid)
    # print(family.FMId)

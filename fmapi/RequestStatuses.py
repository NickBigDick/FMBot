class RequestStatus:

    """
      Заполнение заявки: writing_request
      Модерация : moderation
      Согласование заявки : coordination
      Назначение исполнителя : appointment_executor
      Исполнение заявки : inprogress
      Проверка решения модератором : moderator_check
      Проверка решения инициатором : initiator_check
      Заявка выполнена : ready
      Заявка отменена : canceled

    """
    def __init__(self) -> int:
        self._writing_request = 1
        self._moderation = 2
        self._coordination = 3
        self._appointment_executor = 4
        self._inprogress = 5
        self._moderator_check = 6
        self._initiator_check = 7
        self._ready = 8
        self._canceled = 9


    @property
    def writing_request(self):
        return self._writing_request

    @property
    def moderation(self):
        return self._moderation

    @property
    def coordination(self):
        return self._coordination

    @property
    def appointment_executor(self):
        return self._appointment_executor

    @property
    def inprogress(self):
        return self._inprogress

    @property
    def moderator_check(self):
        return self._moderator_check

    @property
    def initiator_check(self):
        return self._initiator_check

    @property
    def ready(self):
        return self._ready

    @property
    def canceled(self):
        return self._canceled

    def get_requeststatus_by_string(self, string):
        if string == "writing_request":
            return self._writing_request
        elif string == "moderation":
            return self._moderation
        elif string == "coordination":
            return self._coordination
        elif string == "appointment_executor":
            return self._appointment_executor
        elif string == "inprogress":
            return self._inprogress
        elif string == "moderator_check":
            return self._moderator_check
        elif string == "initiator_check":
            return self._initiator_check
        elif string == "ready":
            return self._ready
        elif string == "canceled":
            return self._canceled
        else:
            return None


if __name__ == '__main__':
    # print(RequestStatuses().canceled)
    print(RequestStatus().get_requeststatus_by_string('canceled'))

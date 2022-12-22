class Disciplines:

    """

    Дисциплины и их id

    """
    def __init__(self) -> int:
        self._AR = 9
        self._KR = 12
        self._AI = 10017
        self._TM = 10023
        self._KJC = 10027
        self._VK = 10821
        self._CC = 10828
        self._EOM = 10832
        self._GP = 10836
        self._TX = 10837
        self._KM = 10840
        self._OV = 10841
        self._NC = 10843
        self._O = 10844

    @property
    def AR(self):
        return self._AR
    @property
    def KR(self):
        return self._KR
    @property
    def AI(self):
        return self._AI
    @property
    def TM(self):
        return self._TM
    @property
    def KJC(self):
        return self._KJC
    @property
    def VK(self):
        return self._VK
    @property
    def CC(self):
        return self._CC
    @property
    def EOM(self):
        return self._EOM
    @property
    def GP(self):
        return self._GP
    @property
    def TX(self):
        return self._TX
    @property
    def KM(self):
        return self._KM
    @property
    def OV(self):
        return self._OV
    @property
    def NC(self):
        return self._NC
    @property
    def O(self):
        return self._O

    def get_discipline_by_string(self, string):
        if string == "АР":
            return self._AR
        elif string == "КР":
            return self._KR
        elif string == "АИ":
            return self._AI
        elif string == "ТМ":
            return self._TM
        elif string == "КЖС":
            return self._KJC
        elif string == "ВК":
            return self._VK
        elif string == "СС":
            return self._CC
        elif string == "ЭОМ":
            return self._EOM
        elif string == "ГП":
            return self._GP
        elif string == "ТХ":
            return self._TX
        elif string == "КМ":
            return self._KM
        elif string == "ОВ":
            return self._OV
        elif string == "НС":
            return self._NC
        elif string == "О":
            return self._O

        else:
            return None


if __name__ == '__main__':
    print(Disciplines().NC)
    print(Disciplines().get_discipline_by_string("АР"))

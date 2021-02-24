import inspect


class Module:
    """
    Класс контейнер для хранения загруженного модуля
    и его спецификации
    """

    def __init__(self, moduleObj, specObj):
        self.__moduleObj = self.__CheckModuleType(moduleObj)
        self.__specObj = specObj

    @property
    def Module(self):
        return self.__moduleObj

    @property
    def Scpec(self):
        return self.__specObj

    def __CheckModuleType(self, moduleObj):
        if inspect.ismodule(moduleObj):
            return moduleObj
        raise AttributeError()

    def __str__(self):
        strBuild = f"\n-------------\n"
        strBuild += "Объект модуля\n"
        strBuild += f"Объект {type(self.__moduleObj)}\n"
        strBuild += f"Спецификация {type(self.__specObj)}\n"
        return strBuild
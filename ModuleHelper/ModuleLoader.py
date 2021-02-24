import importlib
from ModuleHelper.Module import Module


class ModuleLoaderHelper:
    """
    Класс для управления внешними модулями системы
    для вызова и запуска модуля должен в нем быть определен главный метод main
    """

    @staticmethod
    def LoadModule(moduleName, filePath):
        spec = importlib.util.spec_from_file_location(moduleName, filePath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return Module(mod, spec)

    @staticmethod
    def ReloadModule(moduleObj):
        if isinstance(moduleObj, Module):
            moduleObj.Scpec.loader.exec_module(moduleObj.Module)
            return
        raise TypeError("Аргумент не является типом 'Module'")


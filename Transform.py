from ProcessHandler import AbstractProcessHandler
from ProcessMessage import ProcessMessage
from Options import TransformOption
from ModuleHelper.ModuleLoader import ModuleLoaderHelper


class Transform(AbstractProcessHandler):
    """
    Класс трансформации данных
    """
    def __init__(self, option: TransformOption):
        self.option = option

    def Handle(self, request: ProcessMessage):
        moduleTransform = ModuleLoaderHelper\
            .LoadModule(
                moduleName="transform_func",
                filePath=self.option.scriptpath
            ).Module
        request.Body = moduleTransform.main(request.Body)
        return super().Handle(request)

from abc import ABC, abstractmethod

from Logger.Logger import LoggingMix
from ProcessMessage import ProcessMessage


class ProcessHandler(ABC, LoggingMix):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def SetNext(self, handler):
        pass

    @abstractmethod
    def Handle(self, df):
        pass


class AbstractProcessHandler(ProcessHandler):

    _nextHandler: ProcessHandler = None

    def SetNext(self, handler: ProcessHandler) -> ProcessHandler:
        self.info(f"Set next handler '{self.__class__.__name__}'")
        self._nextHandler = handler
        return handler

    @abstractmethod
    def Handle(self, request: ProcessMessage):
        if self._nextHandler:
            self.info(f"Process handler '{self.__class__.__name__}'")
            try:
                return self._nextHandler.Handle(request)
            except Exception as e:
                self.error(f"Error process handler '{self.__class__.__name__}'. Info: {e}")
        return None

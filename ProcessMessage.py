from abc import ABC, abstractproperty, abstractmethod
from typing import Any
import pandas as pd


class ProcessMessage:
    """
    Класс сообщения системы.
    Служит для передачи данных между объектами приложения
    """
    __body: pd.DataFrame

    @property
    def Body(self):
        return self.__body

    @Body.setter
    def Body(self, value: pd.DataFrame):
        self.__body = value

    @classmethod
    def Create(cls):
        o = cls()
        return o

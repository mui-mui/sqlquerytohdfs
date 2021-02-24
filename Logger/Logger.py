import logging


class LoggingMix:
    """
    Класс логгера
    """
    def __getattr__(self, name):
        if name in ['critical', 'error', 'warning', 'info', 'debug']:
            if not hasattr(self.__class__, '__logger'):
                self.__class__.__logger = logging.getLogger(self.__class__.__module__)
            return getattr(self.__class__.__logger, name)
        return super(LoggingMix, self).__getattr__(name)

from typing import Optional


class LoadOption:
    """
    Класс опциий загрузки
    """
    connectionString: str
    query: str

    @classmethod
    def Create(cls, connectionString: str, query: str):
        o = cls()
        o.connectionString = connectionString
        o.query = query
        return o


class TransformOption:
    """
    Класс опций трансформации.
    Указывается внешний скрипт.
    """
    scriptpath: str

    @classmethod
    def Create(cls, scriptpath: str):
        o = cls()
        o.scriptpath = scriptpath
        return o


class WriteOption:
    """
    Класс опций писателя данных
    """
    serverHdfs: str
    userHdfs: str
    dirHdfs: str
    filename: str

    @classmethod
    def Create(cls, webHdfsUrl: str, userHdfs: str, dirHdfs: str, filename: str):
        o = cls()
        o.webHdfsUrl = webHdfsUrl
        o.userHdfs = userHdfs
        o.dirHdfs = dirHdfs
        o.filename = filename
        return o

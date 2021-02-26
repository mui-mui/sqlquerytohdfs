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
    webHdfsUrl: str
    userHdfs: str
    dirHdfs: str
    filename: str
    metadataKey: str  # колонка из df, данные из которой будут записаны в метаданные

    @classmethod
    def Create(cls, webHdfsUrl: str, userHdfs: str, dirHdfs: str, filename: str, metadataKey: str):
        o = cls()
        o.webHdfsUrl = webHdfsUrl
        o.userHdfs = userHdfs
        o.dirHdfs = dirHdfs
        o.filename = filename
        o.metadataKey = metadataKey
        return o

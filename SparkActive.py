from pyspark.sql import SparkSession
import uuid

class SparkActive:
    """
    Класс активации/получение spark контекста
    """
    __sparkCtx = None

    @classmethod
    def GetOrCreate(cls):
        if cls.__sparkCtx is None:
            cls.__sparkCtx = SparkSession.builder.appName(uuid.uuid4().__str__()).getOrCreate()
        return cls.__sparkCtx

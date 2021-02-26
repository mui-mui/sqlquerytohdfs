from typing import Any
from Options import LoadOption
from ProcessHandler import AbstractProcessHandler
from ProcessMessage import ProcessMessage
from SparkActive import SparkActive


class Loader(AbstractProcessHandler):
    """
    Класс загрузки данных из бд с помощью контекста spark
    """
    def __init__(self, options: LoadOption):
        self.options = options
        self.sparkActive = SparkActive.GetOrCreate()

    def Handle(self, request):
        print(f"Execute query: {self.options.query}")
        request.Body = self.sparkActive.read\
            .format("jdbc")\
            .option("url", self.options.connectionString)\
            .option("query", self.options.query)\
            .load()\
            .toPandas()
        return super().Handle(request)

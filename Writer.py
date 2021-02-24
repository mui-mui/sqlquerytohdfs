from ProcessHandler import AbstractProcessHandler
from ProcessMessage import ProcessMessage
from Options import WriteOption
import requests
import io
from pyarrow import parquet


class Writer(AbstractProcessHandler):
    """
    Класс писателя данных в hdfs
    TODO:Добавить запись метаинформации в файл
    """
    def __init__(self, option: WriteOption):
        self.options = option

    def Handle(self, request: ProcessMessage):
        resp = requests.put(
            f"{self.options.serverHdfs}"
            f"{self.options.dirHdfs}/"
            f"{self.options.filename}.parquet?user.name={self.options.userHdfs}&op=CREATE&permission=0777", allow_redirects=False)
        f = io.BytesIO()
        request.Body.to_parquet(f, compression='gzip')
        f.seek(0)
        requests.put(resp.headers["Location"], data=f.read())

        return super().Handle(request)

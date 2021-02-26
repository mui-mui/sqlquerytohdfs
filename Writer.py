from MetadataAdjusterHelper.MetadataAdjusterHelper import MetadataAdjusterHelper
from ProcessHandler import AbstractProcessHandler
from ProcessMessage import ProcessMessage
from Options import WriteOption
import requests
import io


class Writer(AbstractProcessHandler):
    """
    Класс писателя данных в hdfs
    Формирует файл parquet с метаданными и записывает в hdfs
    """
    def __init__(self, option: WriteOption):
        self.options = option

    def Handle(self, request: ProcessMessage):
        resp = requests.put(
            f"{self.options.webHdfsUrl}"
            f"{self.options.dirHdfs}/"
            f"{self.options.filename}.parquet?user.name={self.options.userHdfs}&op=CREATE&permission=0777", allow_redirects=False)
        with io.BytesIO() as parquetFileIO:
            request.Body.to_parquet(parquetFileIO, compression='gzip')
            parquetFileIO.seek(0)
            newParquetFileIO = MetadataAdjusterHelper.AddMetadataParquet(
                parquetFileIO=parquetFileIO,
                customMetadata={"PLATE_ID": request.Body[self.options.metadataKey].values.tolist()}
            )
        with newParquetFileIO as f:
            requests.put(resp.headers["Location"], data=f.read())

        return super().Handle(request)

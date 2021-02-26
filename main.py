import logging
import sys
from ProcessMessage import ProcessMessage
from Loader import Loader
from Transform import Transform
from Writer import Writer
from Options import LoadOption, TransformOption, WriteOption

if __name__ == '__main__':
    connectionString = sys.argv[1]
    query = sys.argv[2]
    webHdfsUrl = sys.argv[3]
    userHdfs = sys.argv[4]
    dirHdfs = sys.argv[5]
    filename = sys.argv[6]
    scriptPath = sys.argv[7]
    metadataKey = sys.argv[8]

    # Настройка логгирования
    logging.basicConfig(level=logging.INFO,
                        # filename='myapp.log',
                        # filemode='w',
                        format='%(asctime)s %(name)s %(levelname)s:%(message)s')

    loaderHandler = Loader(
        LoadOption.Create(
            connectionString=connectionString,
            query=query
        ))

    transformHandler = Transform(
        TransformOption.Create(
            scriptpath=scriptPath
        ))

    writerHandler = Writer(
        WriteOption.Create(
            webHdfsUrl=webHdfsUrl,
            userHdfs=userHdfs,
            dirHdfs=dirHdfs,
            filename=filename,
            metadataKey=metadataKey
        ))

    loaderHandler\
        .SetNext(transformHandler)\
        .SetNext(writerHandler)

    loaderHandler.Handle(ProcessMessage.Create())


import json
from typing import io
from pyarrow import parquet


class MetadataAdjusterHelper:
    @staticmethod
    def AddMetadataParquet(parquetFileIO: io.BinaryIO, customMetadata: dict) -> io.BinaryIO:
        parquetFileIO.seek(0)
        table = parquet.ParquetFile(parquetFileIO).read()
        customMetadataBytes = json.dumps(customMetadata).encode('UTF8')
        existingMetadata = table.schema.metadata
        mergedMetadata = {**{'Custom metadata': customMetadataBytes}, **existingMetadata}
        fixedTable = table.replace_schema_metadata(mergedMetadata)
        parquetFileWithMetaIO = io.BinaryIO()
        parquet.write_table(fixedTable, parquetFileWithMetaIO)
        parquetFileWithMetaIO.seek(0)
        return parquetFileWithMetaIO
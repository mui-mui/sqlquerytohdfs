import json
from typing import io
from pyarrow import parquet
import io


class MetadataAdjusterHelper:
    @staticmethod
    def AddMetadataParquet(parquetFileIO: io.BytesIO, customMetadata: dict) -> io.BytesIO:
        parquetFileIO.seek(0)
        table = parquet.ParquetFile(parquetFileIO).read()
        customMetadataBytes = json.dumps(customMetadata).encode('UTF8')
        existingMetadata = table.schema.metadata
        mergedMetadata = {**{'omk metadata': customMetadataBytes}, **existingMetadata}
        fixedTable = table.replace_schema_metadata(mergedMetadata)
        parquetFileWithMetaIO = io.BytesIO()
        parquet.write_table(fixedTable, parquetFileWithMetaIO)
        parquetFileWithMetaIO.seek(0)
        return parquetFileWithMetaIO
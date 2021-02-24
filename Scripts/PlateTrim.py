#Подгружаемый модуль для трансформации данных по термосканнеру

import json

import pandas as pd
import numpy as np
import pyarrow
from pyarrow import parquet
import io

def cut_scanner(plate_id, total_array, pos):
    """
    TODO: Добавить описание
    :param plate_id:
    :param total_array:
    :param pos:
    :return:
    """

    processStatus = f"{plate_id} successful!"
    try:


        count1 = 0

        for i in range(len(total_array)):
            if np.mean(total_array[i, :]) < 301:
                count1 = count1 + 1
            else:
                break

        count2 = count1
        for i in range(count1, len(total_array)):
            if np.mean(total_array[i, :]) != 300:
                count2 = count2 + 1
            else:
                break

        total_array1 = total_array[count1:count2, :]
        pos_array1 = pos[count1:count2]
        mean = np.mean(total_array1[:, 50])
        count1 = 0

        for i in range(len(total_array1)):
            if np.mean(total_array1[i, :]) < mean - 150:
                count1 = count1 + 1
            else:
                break

        count2 = count1
        for i in range(count1, len(total_array1)):
            if np.mean(total_array1[i, :]) > mean - 150:
                count2 = count2 + 1
            else:
                break

        total_array2 = total_array1[count1:count2, :]
        pos_array2 = pos[count1:count2]
        pos_array2 = pos_array2 - pos_array2[0]
        mean = np.mean(total_array2[:, 50])
        count1 = 0

        for i in range(len(total_array2[0])):
            if np.mean(total_array2[:, i]) < mean - 100:
                count1 = count1 + 1
            else:
                break

        count2 = count1
        for i in range(count1, len(total_array2[0])):
            if np.mean(total_array2[:, i]) > mean - 100:
                count2 = count2 + 1
            else:
                break

        total_array3 = total_array2[:, count1:count2]

        temp_scanner = np.full(200, 0)
        k = 0
        for i in range(199):
            if i != 0:
                while i / 200 > k / len(total_array3):
                    k = k + 1
                temp_scanner[i] = total_array3[k, 40]
            else:
                temp_scanner[i] = total_array3[k, 40]
    except IndexError as e:
        temp_scanner = e
        processStatus = f"{plate_id} error!"

    finally:
        print(processStatus)
    return temp_scanner


def main(df: pd.DataFrame):
    df["LINE"] = df[["PLATE_ID", "LINE", "PLATE_HEAD_POSITION"]].index.map(
        lambda idx: cut_scanner(df["PLATE_ID"][idx].astype(str), np.array(eval(df["LINE"][idx])), np.array(eval(df["PLATE_HEAD_POSITION"][idx])))
    )
    return df


if __name__ == '__main__':

    """
    df = pd.read_parquet(r"C:\work\sqlquerytohdfs\part-00000-c373f1fc-19fd-48a2-83fd-65bf49895f1a-c000.snappy.parquet")


    f = io.BytesIO()
    df.to_parquet(f)
    f.seek(0)

    table = parquet.ParquetFile(f).read()
    custom_metadata_json = {'Sample Number': [12,13,14], 'Date Obtained': 'Tuesday'}
    custom_metadata_bytes = json.dumps(custom_metadata_json).encode('utf8')
    existing_metadata = table.schema.metadata
    merged_metadata = {**{'Record Metadata': custom_metadata_bytes}, **existing_metadata}
    fixed_table = table.replace_schema_metadata(merged_metadata)

    f1 = io.BytesIO()

    parquet.write_table(fixed_table, f1)
    f1.seek(0)
    p = parquet.ParquetFile(f1).read()

    print(json.loads(p.schema.metadata[b"Record Metadata"])['Sample Number'][2])

    #f1.seek(0)
    #print(pd.read_parquet(f1))



    #df = df.drop([0]) #.copy()#202202010158000
    #df1.to_parquet(r"C:\work\sqlquerytohdfs\202202010158000")
    #main(df)
    #print(df1["LINE"])
    #print(df["PLATE_ID"].values)
    #print(eval(df["LINE"][0])[0, :])
    #l = np.array([[1,2,3], [4,5,6]])
    #print(len(l))
    """


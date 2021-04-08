#Подгружаемый модуль для трансформации данных по термосканнеру
import statistics
from functools import partial
import pandas as pd
import numpy as np


def TrimArrays(temperatureArray: list, platePositionArray: list) -> tuple:
    """
    Функция обрезки массива температуры и массива позиции плиты
    :param temperatureArray: двумерный массив температур из колонки 'LINE'
    :param platePositionArray: одномерный массив позиций плиты из колонки 'PLATE_HEAD_POSITION'
    :return:
    """
    newTemperatureArray: list = list()
    newPlatePositionArray: list = list()
    i: int = 0
    for tepArr in temperatureArray:
        if statistics.mean(tepArr) >= 350:
            newTemperatureArray.append(tepArr)
            newPlatePositionArray.append(platePositionArray[i])
        i += 1
    return newTemperatureArray, newPlatePositionArray


def main(df: pd.DataFrame):
    trimArrayPartialFunc = \
        map(lambda pandasTuple: partial(TrimArrays, eval(pandasTuple[1].values[0])), df[["LINE"]].iterrows())

    result = list(map(lambda pandasTuple: trimArrayPartialFunc.__next__()(eval(pandasTuple[1].values[0])),
                      df[["PLATE_HEAD_POSITION"]].iterrows()))

    df[["LINE", "PLATE_HEAD_POSITION"]] = df[["LINE", "PLATE_HEAD_POSITION"]] \
        .assign(LINE=[row[0] for row in result],
                PLATE_HEAD_POSITION=[row[1] for row in result])
    return df



# Модуль функций для импорта

# __all__ - это список публичных объектов данного модуля.
__all__ = [
    "time_counter",
    "choice_songs",
]

from random import sample
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_DOWN


def choice_songs(input_list: list | dict) -> dict:
    """ Принимает list или dict. Возвращает dict с тремя песнями """
    three_random_songs = {}
    match input_list:
        case list():
            items = sample(input_list, 3)
            for i in items:
                three_random_songs[i[0]] = i[1]
        case dict():
            items = sample(sorted(input_list.items()), 3)
            for i in items:
                three_random_songs[i[0]] = i[1]      
    return three_random_songs


def time_counter(song_list: dict) -> float:
    """ Суммирует общее время песен """
    total_time = timedelta(minutes=0, seconds=0)
    for i in song_list.values():
        round_time = Decimal(i).quantize(Decimal("1.00"), ROUND_HALF_DOWN)
        _min, _sec = str(round_time).split(".")
        res = timedelta(minutes=int(_min),seconds=int(_sec))
        total_time = total_time + res                    
    return total_time


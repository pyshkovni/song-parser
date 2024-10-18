# Модуля для запуска скрипта

# Структура модуля для запуска кода

# 0. Импорты
from song_parser import time_counter, choice_songs

# 1. Функции

def main(data):
    return time_counter(choice_songs(data))


# 2. Данные

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


# 3. Инициализационный скрипт

if __name__ == "__main__":
    print(
        main(data=my_favorite_songs),
        main(data=my_favorite_songs_dict),
        sep="\n"
        )


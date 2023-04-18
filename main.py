# Основной файл

from utils import *

# - Последние 5 выполненных (EXECUTED) операций выведены на экран.
    # сорт по дате, т.е. надо по ключу дата вытащить
    # Операции разделены пустой строкой.
    # - Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
    # - Сверху списка находятся самые последние операции (по дате).
    # - Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    # - Номер счета замаскирован и не отображается целиком в формате  **XXXX
    # (видны только последние 4 цифры номера счета).

    # 1 сорт по (EXECUTED)
    # 2 сорт по дате
    # 3 отрезаем 5 последних опер
    # 4 разделяем их пуст строкой
    # 5 формат ДД.ММ.ГГГГ (пример: 14.10.2018).
    # 6 Номер карты в формате  XXXX XX** **** XXXX
    # 7 формат ком счета **XXXX (видны только последние 4 цифры номера счета).

def main():
    path = 'operations.json'
    go_list_of_operations = load_start_2(path)    # загрузка данных
    # print(go_list_of_operations)   ### это для понимаяния вывод, он не нужен так

    # ↓ сортировка по дате ↓
    sorted_list = sorted(go_list_of_operations, key=lambda date: date['date'], reverse=True)

    print((sorted_list[0:5]))   # 5 последних операций

    # for operation in go_list_of_operations:
    #     x = operation.get('state', None)    # выборка по ключу 'state' из списка  go_list_of_operations.list_of_operations
    #     if x == 'EXECUTED' and x != None:   # фильтр по выполненным (EXECUTED) операциям
    #         print(x)


    # x = state_def(go_list_of_operations)
    # print(x)

# main_def = main()


if __name__ == "__main__":
    main()

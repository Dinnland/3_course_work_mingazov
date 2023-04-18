# Основной файл

from utils2 import *
path = 'operations.json'


def main():

    data = load_data_from_file(path)
    data = filter_data(data)
    data = sort_data(data)
    data = format_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()

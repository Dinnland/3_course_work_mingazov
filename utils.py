# Файл с функциями

import json

def load_data_from_file(path):
    """
    Чтение Файла
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def razdel_po_oper_json(path):
    """
    данные файла "operations.json" вносятся в список list_of_operations
    :param path:
    :return:list_of_operations
    """
    load_json = load_data_from_file(path)
    list_of_operations = []
    for operation in load_json:
        list_of_operations.append(operation)
    return list_of_operations





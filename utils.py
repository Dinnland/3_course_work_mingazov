# Файл с функциями
import json
from card import Card


def load_data_from_file(path):
    """
    Чтение Файла
    :param path:
    :return: json.load(file)
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


# def add_json_to_local_list(path):
#     """
#     данные файла "operations.json" вносятся в список list_of_operations
#     :param path:
#     :return:list_of_operations
#     """
#     load_json = load_data_from_file(path)
#     list_of_operations = []
#     for operation in load_json:
#         list_of_operations.append(operation)
#     return list_of_operations

def load_start(path):
    """
    Cписок экземпляров класса Start.(При старте программы
    данные считываются и раскладываются в экземпляры класса Start.
    Все экземпляры складываются в список list_of_operations.)
    """
    data = load_data_from_file(path)
    list_of_operations = []
    for operation in data:
        x = operation.get('state', '______')  # выборка по ключу 'state' из списка  go_list_of_operations.list_of_operations
        if x == 'EXECUTED' and x != None and x != '______':   # фильтр по выполненным (EXECUTED) операциям
            if operation.get('from') == None:
                list_of_operations.append(
                    Card(
                        state=operation['state'],
                        date=operation['date'],
                        description=operation['description'],

                        to=operation['to'],
                        amount=operation["operationAmount"]["amount"],
                        name=operation["operationAmount"]['currency']['name']
                    )
                )
            else:
                list_of_operations.append(
                    Card(
                        state=operation['state'],
                        date=operation['date'],
                        description=operation['description'],
                        from_=operation['from'],
                        to=operation['to'],
                        amount=operation["operationAmount"]["amount"],
                        name=operation["operationAmount"]['currency']['name']
                    )
                )
            # list_of_operations.append(operation.get('from','________'))



    return list_of_operations


    # list_of_operations.append(
    #             Card(
    #                 state=operation['state'],
    #                 date=operation['date'],
    #                 description=operation['description'],
    #                 from_=operation['from'],
    #                 to=operation['to'],
    #                 amount=operation["operationAmount"]["amount"],
    #                 name=operation["operationAmount"]['currency']['name']
    #             )
    #         )







# def state_def(list_op):
#
#     for operation in list_op:
#         # print(operation.get('state', None))
#         x = operation.get('date')
#
#         # if x == 'EXECUTED' and x != 'hui':
#     return x

    # for operation in list_op:
    #     x = operation.get('date', 'hui')
    #
    #     # if x == 'EXECUTED' and x != 'hui':
    # return x


# g = add_json_to_local_list('operations.json')
# print(g)

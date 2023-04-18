
import json


def load_data_from_file(path):
    """
    Чтение Файла
    :param path:
    :return: json.load(file)
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def h():
    operation = []
    for oper in data:
        if not (oper.get('from') and oper.get('state')):
            continue
        if oper['state'] == 'EXECUTED':
            date = datetime.datetime.strptime(oper['date'], '%Y-%m-%dT%H:%M:%S.%f')
            date = date.strftime('%d.%m.%Y ')
            # if 'Счет' in oper['from']:
            #     from_ = oper['from'].split()

            operation.append({'date': date,
                              'description': oper['description'],
                              'from': oper['from'],
                              'to': oper['to'],
                              'amount': oper['operationAmount']["amount"],
                              'currency_name': oper['operationAmount']["currency"]["name"]
                              })

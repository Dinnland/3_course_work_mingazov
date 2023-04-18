# файл с функциями
import json
import datetime


def load_data_from_file(path):
    """
    Чтение json Файла
    :param path:
    :return: data
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filter_data(data):
    """
    Возвращает выполненные 'EXECUTED' операции
    :param data:
    :return: 'EXECUTED' data
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    """
    возращает x['date']
    :param x:
    :return: x['date']
    """
    return x['date']


def sort_data(data):
    """
    Возвращает отсортированный список по дате
    :param data:
    :return: data[:5]
    """
    # print([x['date'] for x in data])
    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def metod_check(roww):
    """
    Функция форматирует в нужный вид номер счета
    :param roww:
    :return: sender_recipient_info, sender_recipient_bill
    """
    sender_recipient = roww.split()
    sender_recipient_info = sender_recipient[0]  # название счета отправителя
    len_check = len(roww)  # длина номера счета
    # ↓ форматированный номер счета отправителя ↓
    sender_recipient_bill = "**" + roww[len_check - 4:len_check]  # "**" + последние 4 цифры счета
    return sender_recipient_info, sender_recipient_bill


def metod_card(roww):
    """
    Функция форматирует в нужный вид номер скарты
    :param roww:
    :return: sender_recipient_info, sender_recip_bill
    """
    sender_recipient = roww.split()
    sender_recip_bill = sender_recipient.pop(-1)  # номер карты отправителя
    sender_recipient_info = " ".join(sender_recipient)  # название карты отправителя
    # ↓ форматированный номер карты отправителя ↓
    sender_recip_bill = f"{sender_recip_bill[:4]} {sender_recip_bill[4:6]}** **** {sender_recip_bill[-4:]}"
    return sender_recipient_info, sender_recip_bill


def format_data(data):
    formatted_data = []  # необходимый вид вывода информации
    for row in data:  # перебор каждой операции в списке данных
        # ↓ форматирование даты в нужный вид ↓
        date = datetime.datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f')
        date = date.strftime('%d.%m.%Y')
        # ↓ количественное выражение денежной массы ↓
        amount = row['operationAmount']['amount']
        currency_name = row['operationAmount']['currency']['name']  # валюта
        description = row['description']  # описание операции
        from_arrow = ''  # from_arrow: '->' или пустая строка.   PIP8 ругается, но я оставил на всякий

        # ↓ метод работы для 'from' ↓
        if 'from' in row:  # если есть ключ 'from'
            from_arrow = "->"
            roww = row['from']
            if 'Счет' in row['from']:  # для счета
                def_metod_check = metod_check(roww)
                sender_info, sender_bill = def_metod_check
            else:  # для карты
                def_metod_card = metod_card(roww)
                sender_info, sender_bill = def_metod_card
        else:  # если нет ключа 'from'
            sender_info = 'Открытие счета/вклада:'
            sender_bill = ''
            from_arrow = ''

        # ↓ метод работы для 'to' ↓
        if 'to' in row:  # если есть ключ 'to'
            roww = row['to']
            if 'Счет' in row['to']:  # для счета
                def_metod_check = metod_check(roww)
                recipient_info, recipient_bill = def_metod_check
            else:
                def_metod_card = metod_card(roww)
                recipient_info, recipient_bill = def_metod_card
        else:  # если нет ключа 'to'
            recipient_info = 'нет данных адреса отправления'
            recipient_bill = '-'

        formatted_data.append(f"""
    {date} {description}
    {sender_info} {sender_bill} {from_arrow} {recipient_info} {recipient_bill}
    {amount} {currency_name}
        """)
    return formatted_data

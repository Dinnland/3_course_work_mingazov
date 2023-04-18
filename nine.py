import json
import datetime
import re

# g = [1,4,234,6,4534,23,42234,2]
# print(g)
# print(sorted(g))
# ff = []
# # for i in range(5):
# #     for t in g:
# #         ff.append()
# print(len(g))
# print(g[0:5])


with open('operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

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

print(operation)
print(len(operation))
# sorted_list = sorted(operation, key=lambda date: date['date'] )
# print(sorted_list)
# print(operation['from'])


for y in operation:
    # ↓ проверка 'куда'/'to' отправляются деньги ↓
    if 'Счет' in y.get('to'):
        len_check = len(y['to'])  # длина номера счета
        check_card_to = "Счет **" + y['to'][len_check - 4:len_check]  # последние 4 цифры счета
    else:
        check_card_to = y['to']  # шифрование номера карты

    # ↓ проверка 'откуда'/'from' отправляются деньги ↓
    if 'Счет' in y.get('from'):
        len_check = len(y['from'])  # длина номера счета
        check_card_from = "Счет **" + y['from'][len_check - 4:len_check]  # последние 4 цифры счета
    else:
        check_card_from = y['from']  # шифрование номера карты

    print(f"{y['date']} {y['description']}\n"
          f"{check_card_from} -> {check_card_to}\n"
          f"{y['amount']} {y['currency_name']}\n")


# разделение по циф букв

def diff_abc_numbers(abc_numb):
    """
    разделяет номер карты на буквы и цифры
    :param abc_numb:
    :return: [chars, nums]
    """
    # x = 'Visa Classic 6831982476737658'

    chars = re.findall(r'[a-zA-Z]+', abc_numb)  # ['k', 'e', 'g', 'f']
    nums = re.findall(r'\d+', abc_numb)  # ['3', '10', '88', '13']

    return [chars, nums]
diff_abc_n = diff_abc_numbers('Visa Classic 6831982476737658')
print(diff_abc_n)

from utils import utils


# from utils.utils import sort_data


def test_sort_data(test_data):
    sorted_data = utils.sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                                                '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075']


def test_filter_data(test_data2):
    assert utils.filter_data(test_data2) == [{'date': '2018-03-23T10:45:06.972075',
                                              'description': 'Открытие вклада',
                                              'id': 587085106,
                                              'operationAmount': {'amount': '48223.05',
                                                                  'currency': {'code': 'RUB', 'name': 'руб.'}},
                                              'state': 'EXECUTED',
                                              'to': 'Счет 41421565395219882431'}]


def test_method_check():
    # def test_metod_check():
    assert utils.metod_check("Счет 64686473678894779589") == ('Счет', '**9589')
    assert utils.metod_check("Master Card 1435442169918409") == ('Master', '**8409')


def test_metod_card():
    assert utils.metod_card("Maestro 1596837868705199") == ('Maestro', '1596 83** **** 5199')
    assert utils.metod_card("Master Card 1435442169918409") == ('Master Card', '1435 44** **** 8409')


def test_format_data2(test_data2):
    assert utils.format_data(test_data2) == ['\n'
                                             '    23.03.2018 Открытие вклада\n'
                                             '    Открытие счета/вклада:   Счет **2431\n'
                                             '    48223.05 руб.\n'
                                             '        ']


def test_format_data(test_data):
    assert utils.format_data(test_data) == ['\n'
                                            '    26.08.2019 Перевод организации\n'
                                            '    Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                            '    31957.58 руб.\n'
                                            '        ',
                                            '\n'
                                            '    03.07.2019 Перевод организации\n'
                                            '    MasterCard 7158 30** **** 6758 -> Счет **5560\n'
                                            '    8221.37 USD\n'
                                            '        ',
                                            '\n'
                                            '    30.06.2018 Перевод организации\n'
                                            '    Счет **6952 -> Счет **6702\n'
                                            '    9824.07 USD\n'
                                            '        ',
                                            '\n'
                                            '    23.03.2018 Открытие вклада\n'
                                            '    Открытие счета/вклада:   Счет **2431\n'
                                            '    48223.05 руб.\n'
                                            '        ']

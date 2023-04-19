import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    # assert arrs.get([1, 2, 3], 1, "test") == 2
    # self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
    def test_sort_data(self):
        self.sorted_data = utils.sort_data([
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }])
        self.assertEqual([x['date'] for x in self.sorted_data],
                         ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364',
                          '2018-06-30T02:08:58.425572'])

    def test_filter_data(self):
        test_data2 = [{
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]
        self.assertEqual(utils.filter_data(test_data2), [{'date': '2018-03-23T10:45:06.972075',
                                                          'description': 'Открытие вклада',
                                                          'id': 587085106,
                                                          'operationAmount': {'amount': '48223.05',
                                                                              'currency': {'code': 'RUB',
                                                                                           'name': 'руб.'}},
                                                          'state': 'EXECUTED',
                                                          'to': 'Счет 41421565395219882431'}])

    def test_method_check(self):
        # def test_metod_check():
        self.assertEqual(utils.metod_check("Счет 64686473678894779589"), ('Счет', '**9589'))
        self.assertEqual(utils.metod_check("Master Card 1435442169918409"), ('Master', '**8409'))

    def test_metod_card(self):
        self.assertEqual(utils.metod_card("Maestro 1596837868705199"), ('Maestro', '1596 83** **** 5199'))
        self.assertEqual(utils.metod_card("Master Card 1435442169918409"), ('Master Card', '1435 44** **** 8409'))

    #
    def test_format_data2(self):
        test_data2 = [{
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]
        self.assertEqual(utils.format_data(test_data2), ['\n'
                                                         '    23.03.2018 Открытие вклада\n'
                                                         '    Открытие счета/вклада:   Счет **2431\n'
                                                         '    48223.05 руб.\n'
                                                         '        '])

    def test_format_data(self):
        test_data = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }]
        self.assertEqual(utils.format_data(test_data), ['\n'
                                                        '    26.08.2019 Перевод организации\n'
                                                        '    Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                                        '    31957.58 руб.\n'
                                                        '        ',
                                                        '\n'
                                                        '    03.07.2019 Перевод организации\n'
                                                        '    MasterCard 7158 30** **** 6758 -> Счет **5560\n'
                                                        '    8221.37 USD\n'
                                                        '        ',
                                                        ])


if __name__ == '__main__':
    unittest.main()

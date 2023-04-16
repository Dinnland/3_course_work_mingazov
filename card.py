class Card:
    def __init__(self, state='', date='', description='',
                 from_='Нет информации',to='',amount='',name=''):
        self.state = state              # статус операции
        self.date = date                # дата перевода
        self.description = description  # описание перевода
        self.from_ = from_              # откуда
        self.to = to                    # куда
        self.amount = amount            # cумма перевода
        self.name = name                # валюта
        
    def start(self):
        return f'{self.date}{self.description}{self.from_}' \
               f'{self.to}{self.amount}{self.name}'
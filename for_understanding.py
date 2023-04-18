import datetime
import re
g = [{
   'rd':3,
   'd':4
},{
   'e':{'g':5,'gg':5},
   'r':4
},{
   'rr':3,
   'gg':4
}]

# for operation in g:
#    print(operation.get('e'('g')))

date = datetime.datetime.strptime('2019-08-26T10:50:58.294041', '%Y-%m-%dT%H:%M:%S.%f')
# print(f'{date:%d.%m.%Y}')


txt = 'one one was a race horse, two two was one too.'
x = txt.replace('one', 'three')
# print(x)

rfr = '23423423235'
# print(len(rfr))
# d = rfr.replace()


card = "visa classic 2842878893689012"
card_number = card.split()[-1]
card_names = card.split()
card_full_name = card_names[0:len(card_names) - 1]
print('card_name', card_full_name)
print(card_number)

private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]

chunks, chunk_size = len(private_number), len(private_number)//4
print(" ".join(card_full_name)," ".join([private_number[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]))


# card = "Visa Classic 2842878893689012"
# card_number = card.split()[-1]
# print(card_number)
# private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
#
# chunks, chunk_size = len(private_number), len(private_number)//4
# print(" ".join([ private_number[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]))
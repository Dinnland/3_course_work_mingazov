import datetime

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
print(f'{date:%d.%m.%Y}')
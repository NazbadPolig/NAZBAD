#Програма дізнається скільки років користувачу. Запушити на гитхаб
#import datetime
#a=datetime.date.today()
#b=datetime.datetime(int(input('rik')),int(input('misyac')),int(input('den')),hour=21,minute=35,second=34,microsecond=321)
#print(a)
rik=2022
misyac=11
b=int(input('rik narodgenya'))
c=int(input('misyac narodgenya'))
n=((rik*12)+misyac)-((b*12)+c)
print(n/12)
from datetime import date,timedelta,datetime

#1
x = date.today() - timedelta(days=5)
print(x,"\n")

#2
x = date.today()
print("Yesterday:",x-timedelta(days=1))
print("Today:",x)
print("Tomorrow",x+timedelta(days=1),"\n")

#3
my_datetime = datetime.now()
print(my_datetime.replace(microsecond=0),"\n")

#4
first = datetime(2024,2,1, 10,34,50)
second = datetime(2023,12,17, 9,29,56)

print(abs(first.second - second.second),"\n")
from datetime import datetime, date, time

d1 = date.today()
t1 = time(7, 37, 20)
dt1 = datetime.now()
#print(d1)
#print(t1)
#print(dt1)

print(d1.day)
print(d1.year)
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

print(days[d1.weekday()])

#modidy values with replace
d1 = d1.replace(year=2020)
t1 = t1.replace(hour=15)
dt1 = dt1.replace(month=5)

print(d1)
print(t1)
print(dt1)
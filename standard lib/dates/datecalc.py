from datetime import datetime, timedelta

dt1 = datetime(2022, 1, 1, 10, 15)
dt2 = datetime(2022, 1, 6, 15, 15)

#compare dates
print( dt1 < dt2)
print( dt1 > dt2)
#subtracting one date from the order to create a timedelta

delta = dt2 - dt1
print(delta.days)
print(delta.seconds)


now = datetime.now()
oneyear = timedelta(days=365)
oneweek = timedelta(weeks=1)

print('One year from now is:', now +oneyear)
print('One week from now is:', now + oneweek)
print('One year ago is:', now - oneyear)
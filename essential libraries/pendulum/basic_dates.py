import pendulum
from datetime import datetime
import time

date1 = pendulum.datetime(2022, 2, 9)
#print(isinstance(date1, datetime))
#print(date1.timezone.name)
date2 = pendulum.datetime(2022, 2, 9, tz='America/Chicago')
#print(date2)

date3 = date2.in_timezone('UTC')
#print(date3)
date_here = pendulum.local(2020,10,10)
#print(date_here.timezone.name)

today = pendulum.today()
tomorrow = pendulum.tomorrow()
yesterday = pendulum.yesterday('America/New_York')

#print(today, tomorrow, yesterday)
time1 = time.time()

dt = pendulum.from_timestamp(time1)
#print(dt)

dt1 = pendulum.datetime(2022, 2, 9, 15, 28)

print(dt1.to_date_string())
print(dt1.to_time_string())
print(dt1.to_datetime_string())

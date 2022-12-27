import datetime
from dateutil import tz

d1 = datetime.datetime(2022, 3, 12, 6, 15, tzinfo=tz.gettz('Europe/Madrid'))
d2 = datetime.datetime(2022, 3, 12, 5, 15, tzinfo=tz.gettz('America/Los_Angeles'))
print(d1.hour > d2.hour)
print(d1 > d2)

d2_madrid = d2.astimezone(tz.gettz('Europe/Madrid'))

print(d2_madrid)

"""
Exercise 88: Calculating the Time Delta between Two datetime Objects
"""

d1 = datetime.datetime(2019, 2, 25, 10, 50, tzinfo=datetime.timezone.utc)
d2 = datetime.datetime(2019, 2, 26, 11, 20, tzinfo=datetime.timezone.utc)
print(d2 -d1)
d1 = datetime.datetime(2019, 2, 25, 10, 50)
d2 = datetime.datetime(2019, 2, 26, 11, 20)
print(d2 -d1)
td = d2 - d1
print(td.total_seconds())

d1 = datetime.datetime.now(datetime.timezone.utc)
print(d1.isoformat())


"""
Exercise 89: Calculating the Unix Epoch Time
"""
import time

time_now = time.time()
datetime_now = datetime.datetime.now(datetime.timezone.utc)


epoch  = datetime_now - datetime.timedelta(seconds=time_now)
print(time_now)
print(datetime_now)
print(datetime.timedelta(seconds=time_now))
print(epoch)

import calendar

c = calendar.Calendar()

days = list(c.itermonthdates(2022, 2))

for day in days:
    print(day)

print("==========")
days = list(d for d in c.itermonthdates(2022, 2) if d.month == 2)

for day in days:
    print(day)


"""
Activity 15: Calculating the Time Elapsed to Run a Loop
"""
import random

init_time = time.time()
l = [random.randint(1, 999) for _ in range(10 * 3)]
end_time = time.time()

delta = end_time - init_time

print(delta)


init_time = time.time_ns()
l = [random.randint(1, 999) for _ in range(10 * 3)]
end_time = time.time_ns()

delta = end_time - init_time

print(delta)

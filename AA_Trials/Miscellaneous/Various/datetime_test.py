import datetime as dt
from time import sleep

time1 = dt.datetime.now()

sleep(5)

time2 = dt.datetime.now()

print((time2 - time1).total_seconds())

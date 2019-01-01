from datetime import datetime
from datetime import timedelta


t = timedelta(days=4, hours=10)

type(t)
# <class 'datetime.timedelta'>

t.days
# 4

t.seconds
# 36000

t.hours
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'datetime.timedelta' object has no attribute

t.seconds / 60 / 60
# 10.0

t.seconds / 3600
# 10.0

##############

eta = timedelta(hours=6)

today = datetime.today()

today
# datetime.datetime(2019, 1, 1, 18, 37, 59, 638263)

eta
# datetime.timedelta(0, 21600)

today + eta
# datetime.datetime(2019, 1, 2, 0, 37, 59, 638263)

str(today + eta)
# '2019-01-02 00:37:59.638263'




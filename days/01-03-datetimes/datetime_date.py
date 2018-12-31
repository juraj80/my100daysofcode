#!python3shell

from datetime import datetime
from datetime import date

datetime.today()
# datetime.datetime(2018, 12, 31, 12, 19, 31, 688211)

today = datetime.today()

type(today)
# <class 'datetime.datetime'>





todaydate = date.today()

todaydate
# datetime.date(2018, 12, 31)

type(todaydate)
# <class 'datetime.date'>

todaydate.month
# 12
todaydate.day
# 31
todaydate.year
# 2018

christmas = date(2018,12,25)

christmas
# datetime.date(2018, 12, 25)

christmas - todaydate
# datetime.timedelta(-6)

(christmas - todaydate).days
# -6


if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " days until Christmas!")
else:
    print("Yay it's Christmas!")

# Sorry there are still-6 until Christmas!
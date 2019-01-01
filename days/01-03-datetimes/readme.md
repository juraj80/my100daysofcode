# Days 01-03 Dealing with Datetimes


**1. datetime object**

```
from datetime import datetime

datetime.today()
# datetime.datetime(2018, 12, 31, 12, 19, 31, 688211)

today = datetime.today()

type(today)
# <class 'datetime.datetime'>

```

Use: for the exact timestamps or logging

**2. date object**

```
from datetime import date

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
```

**3. timedelta object**


import timeit
from datetime import datetime
import calendar

def timed(func):
    t0 = datetime.now()

    func()

    dt = datetime.now() - t0
    print("Time: {:,.3f} ms".format(dt.total_seconds() * 1000.0), flush=True)

## timeit - measure execution time of small code snippets

### Command-Line Interface

# python3 - m timeit '"-".join(str(n) for n in range(100))'

### Python Interface

# import timeit
# timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)


### Examples

# mydata = 5
# def f1(x):
#     return x+1
# print(timeit.timeit("f1(mydata)", setup = "from __main__ import f1, mydata", number=1))


# list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):

            yield year
timed(leap_years_lst)
print(timeit.timeit("leap_years_lst", setup = "from __main__ import leap_years_lst", number=1))

timed(leap_years_gen)
print(timeit.timeit("leap_years_gen", setup = "from __main__ import leap_years_gen", number=1))




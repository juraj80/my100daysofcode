import time
from functools import wraps

def timeit(func):
    '''Decorator to time a function'''
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('==Starting timer')
        print()
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print()
        print(f'==Function {func.__name__} took {int(end-start)} seconds to complete')
    return wrapper

@timeit
def generate_report():
    print("Generating report")
    time.sleep(2)
    print("Done.")


generate_report()
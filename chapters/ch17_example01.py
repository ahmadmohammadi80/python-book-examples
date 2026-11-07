# Python book chapter 17, example 1
from functools import wraps

def announce(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("شروع:", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 5))

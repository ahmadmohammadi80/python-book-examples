# Python book chapter 17, worked practice
from functools import wraps

def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(fn.__name__, "=>", result)
        return result
    return wrapper

@trace
def square(x: int) -> int:
    return x * x

print(square(4))

# Python book chapter 13, example 1
def safe_divide(a, b):
    if b == 0:
        raise ValueError("مخرج نباید صفر باشد")
    return a / b

try:
    print(safe_divide(10, 0))
except ValueError as exc:
    print("خطا:", exc)

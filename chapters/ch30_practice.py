# Python book chapter 30, worked practice
def reserve(stock, qty):
    if not isinstance(stock, int) or not isinstance(qty, int):
        raise TypeError("موجودی و تعداد باید صحیح باشند")
    if stock < 0 or qty <= 0 or qty > stock:
        raise ValueError("درخواست نامعتبر")
    return stock - qty

assert reserve(5, 2) == 3
try:
    reserve(1, 2)
except ValueError:
    print("درخواست بیش از موجودی رد شد")

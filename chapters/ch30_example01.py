# Python book chapter 30, example 1
def reserve(stock: int, requested: int) -> int:
    if requested <= 0:
        raise ValueError("تعداد باید مثبت باشد")
    if requested > stock:
        raise ValueError("موجودی کافی نیست")
    return stock - requested

print(reserve(7, 3))

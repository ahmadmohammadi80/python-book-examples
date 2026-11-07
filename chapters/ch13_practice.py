# Python book chapter 13, worked practice
def quantity(raw):
    try:
        n = int(raw)
    except ValueError as err:
        raise ValueError("تعداد باید عدد صحیح باشد") from err
    if n <= 0:
        raise ValueError("تعداد باید مثبت باشد")
    return n

for sample in ["3", "0", "abc"]:
    try:
        print(quantity(sample))
    except ValueError as error:
        print("رد شد:", error)

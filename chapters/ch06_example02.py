# Python book chapter 06, example 2
stock = 8
requested = 3
active = True
if active and 0 < requested <= stock:
    print("ثبت سفارش مجاز است")
else:
    print("درخواست نامعتبر یا موجودی ناکافی")

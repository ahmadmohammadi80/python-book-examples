# Python book chapter 02, worked practice
from decimal import Decimal
price = Decimal("149.90")
count = 3
total = price * count
discount = total * Decimal("0.10")
print("قابل پرداخت:", total - discount)
assert total == Decimal("449.70")

# Python book chapter 02, example 1
unit_price = 125_000
quantity = 3
discount = 0.10
subtotal = unit_price * quantity
total = subtotal * (1 - discount)
print(f"قابل پرداخت: {total:,.0f}")

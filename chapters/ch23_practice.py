# Python book chapter 23, worked practice
def calculate_total(lines):
    total = 0
    for price, quantity in lines:
        if price < 0 or quantity <= 0:
            raise ValueError("سطر سفارش نامعتبر")
        total += price * quantity
    return {"total": total}

print(calculate_total([(25000, 2), (10000, 1)]))

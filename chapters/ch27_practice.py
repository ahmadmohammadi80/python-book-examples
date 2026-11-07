# Python book chapter 27, worked practice
transactions = [("income", 500000), ("expense", 120000), ("expense", 30000)]
def balance(rows):
    total = 0
    for kind, amount in rows:
        if amount < 0 or kind not in {"income", "expense"}:
            raise ValueError("تراکنش نامعتبر")
        total += amount if kind == "income" else -amount
    return total

print(balance(transactions))

# Python book chapter 27, example 2
transactions = [("income", 800000), ("expense", 250000), ("expense", 90000)]
income = sum(amount for kind, amount in transactions if kind == "income")
expense = sum(amount for kind, amount in transactions if kind == "expense")
print("مانده:", income - expense)

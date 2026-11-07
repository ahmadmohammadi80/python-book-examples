# Python book chapter 09, example 1
products = [{"name": "A", "price": 80}, {"name": "B", "price": 140}]
affordable = [p["name"] for p in products if p["price"] <= 100]
print(affordable)

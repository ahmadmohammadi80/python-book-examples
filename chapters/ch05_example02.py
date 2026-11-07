# Python book chapter 05, example 2
product = {"name": "ماوس", "price": 450000, "stock": 12}
product["stock"] -= 2
print(product["name"], product.get("stock"))

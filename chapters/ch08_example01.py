# Python book chapter 08, example 1
def final_price(price: float, discount: float = 0) -> float:
    if price < 0 or not 0 <= discount <= 1:
        raise ValueError("مقدار نامعتبر است")
    return price * (1 - discount)

print(final_price(200000, 0.15))

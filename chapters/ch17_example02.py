# Python book chapter 17, example 2
def average(values: list[float]) -> float:
    if not values:
        raise ValueError("فهرست خالی است")
    return sum(values) / len(values)

print(average([12.0, 16.0, 17.0]))

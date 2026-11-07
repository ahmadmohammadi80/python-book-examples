# Python book chapter 14, example 2
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    stock: int = 0

p = Product("کتاب", 150000, 4)
print(p)

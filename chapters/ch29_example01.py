# Python book chapter 29, example 1
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: int

def validate_item(item: Item):
    if not item.name.strip() or item.price < 0:
        raise ValueError("کالای نامعتبر")
    return item

print(validate_item(Item("دفتر", 100000)))

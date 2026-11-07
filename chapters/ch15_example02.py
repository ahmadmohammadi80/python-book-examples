# Python book chapter 15, example 2
class Inventory:
    def __init__(self):
        self.stock = {}

class Shop:
    def __init__(self, inventory):
        self.inventory = inventory

store = Shop(Inventory())
print(isinstance(store.inventory, Inventory))

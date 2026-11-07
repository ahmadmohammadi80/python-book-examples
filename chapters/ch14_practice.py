# Python book chapter 14, worked practice
class Wallet:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("موجودی نامعتبر")
        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            raise ValueError("برداشت نامعتبر")
        self._balance -= amount
        return self._balance

wallet = Wallet(100)
print(wallet.withdraw(30))

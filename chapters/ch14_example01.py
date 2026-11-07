# Python book chapter 14, example 1
class Account:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("موجودی منفی")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("مبلغ نامعتبر")
        self.balance += amount

account = Account("آرزو", 100)
account.deposit(50)
print(account.balance)

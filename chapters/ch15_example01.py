# Python book chapter 15, example 1
class CashPayment:
    def pay(self, amount):
        return f"نقدی: {amount}"

class CardPayment:
    def pay(self, amount):
        return f"کارتی: {amount}"

def checkout(payment, amount):
    return payment.pay(amount)

print(checkout(CardPayment(), 90000))

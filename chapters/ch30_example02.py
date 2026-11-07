# Python book chapter 30, example 2
import unittest

def reserve(stock, qty):
    if qty <= 0 or qty > stock:
        raise ValueError("نامعتبر")
    return stock - qty

class TestInventory(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(reserve(5, 2), 3)
    def test_reject(self):
        with self.assertRaises(ValueError):
            reserve(1, 3)

result = unittest.TestResult()
TestInventory("test_ok").run(result)
TestInventory("test_reject").run(result)
print("موفق:", result.wasSuccessful())

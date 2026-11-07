# Python book chapter 24, worked practice
from statistics import mean, median

prices = [100, 120, 130, 150, 900]
print("میانگین:", mean(prices))
print("میانه:", median(prices))
assert mean(prices) > median(prices)

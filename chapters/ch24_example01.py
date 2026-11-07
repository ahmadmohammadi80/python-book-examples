# Python book chapter 24, example 1
from statistics import mean, median, pstdev

prices = [100, 120, 110, 800, 105]
print("میانگین:", mean(prices))
print("میانه:", median(prices))
print("انحراف معیار جامعه:", round(pstdev(prices), 2))

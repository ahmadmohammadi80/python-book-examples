# Python book chapter 18, example 1
from collections import Counter

words = ["python", "data", "python", "web"]
print(Counter(words).most_common(2))

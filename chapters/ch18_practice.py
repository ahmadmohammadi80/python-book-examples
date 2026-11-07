# Python book chapter 18, worked practice
from collections import Counter
from datetime import date, timedelta

orders = ["کتاب", "دفتر", "کتاب", "مداد", "کتاب"]
print(Counter(orders).most_common(1))
print(date(2026, 11, 6) + timedelta(days=7))

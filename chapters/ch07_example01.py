# Python book chapter 07, example 1
numbers = [3, -2, 5, 0, 8]
total = 0
for n in numbers:
    if n <= 0:
        continue
    total += n
print("جمع اعداد مثبت:", total)

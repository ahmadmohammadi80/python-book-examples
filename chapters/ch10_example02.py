# Python book chapter 10, example 2
values = [4, 2, 4, 1, 2, 4]
counts = {}
for value in values:
    counts[value] = counts.get(value, 0) + 1
print(counts)

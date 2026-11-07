# Python book chapter 07, worked practice
values = [6, 11, 0, 13, -2]
valid = []
for value in values:
    if value < 0:
        break
    if value == 0:
        continue
    valid.append(value)
print(valid)
assert valid == [6, 11, 13]

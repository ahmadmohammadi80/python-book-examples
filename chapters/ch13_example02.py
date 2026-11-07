# Python book chapter 13, example 2
raw = ["12", "x", "8"]
valid = []
for item in raw:
    try:
        valid.append(int(item))
    except ValueError:
        print("رد شد:", item)
print(valid)

# Python book chapter 09, worked practice
raw = ["12", "x", "19", "-1"]
parsed = []
for token in raw:
    try:
        parsed.append(int(token))
    except ValueError:
        pass
positive = [n for n in parsed if n > 0]
print(positive)

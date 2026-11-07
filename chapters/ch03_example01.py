# Python book chapter 03, example 1
def parse_positive_int(text):
    try:
        value = int(text)
    except ValueError:
        return None
    return value if value > 0 else None

for sample in ["8", "-2", "abc"]:
    print(sample, parse_positive_int(sample))

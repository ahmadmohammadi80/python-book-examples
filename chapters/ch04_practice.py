# Python book chapter 04, worked practice
def normalize_spaces(text):
    return " ".join(text.strip().split())

samples = ["  کلاس    پایتون  ", "", "Python   3"]
for item in samples:
    clean = normalize_spaces(item)
    print(repr(clean), len(clean.split()))

# Python book chapter 03, worked practice
def parse_age(raw):
    raw = raw.strip()
    try:
        age = int(raw)
    except ValueError:
        return None
    return age if 0 <= age <= 120 else None

for s in [" 20 ", "-3", "abc"]:
    print(repr(s), parse_age(s))

# Python book chapter 05, worked practice
votes = ["آبی", "قرمز", "آبی", "سبز", "قرمز", "آبی"]
counts = {}
for color in votes:
    counts[color] = counts.get(color, 0) + 1
print(counts)
assert sum(counts.values()) == len(votes)

# Python book chapter 10, worked practice
def unique_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(unique_keep_order([3, 1, 3, 2, 1]))

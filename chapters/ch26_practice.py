# Python book chapter 26, worked practice
def average_grade(grades):
    if not grades:
        return None
    if any(not 0 <= x <= 20 for x in grades):
        raise ValueError("نمره خارج از بازه")
    return sum(grades) / len(grades)

print(average_grade([14, 18, 16]))
print(average_grade([]))

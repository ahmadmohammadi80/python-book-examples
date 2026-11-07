# Python book chapter 16, worked practice
def positive_numbers(items):
    for number in items:
        if number > 0:
            yield number

stream = positive_numbers([2, -1, 5])
print(list(stream))
print(list(stream))
print(list(positive_numbers([2, -1, 5])))

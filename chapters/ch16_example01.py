# Python book chapter 16, example 1
def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number

for n in even_numbers(8):
    print(n)

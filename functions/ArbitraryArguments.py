# Sum function gets 2 arguments, first number given, and an unfixed amount of numbers, and will sum them all.
# b argument is a tuple, so in order to read all numbers we use a for loop.
def sum(a, *b):
    result = a
    for element in b:
        result += element
    return result

print(sum(5,5,5,5,5,6))
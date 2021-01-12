# Sum function gets 2 arguments, first number given, and an unfixed amount of numbers, and will sum them all.
# b argument is a tuple, so in order to read all numbers we use a for loop.
def sum(a, *b):
    result = a
    for element in b:
        result += element
    return result


print(sum(5,5,5,5,5,6))


# LAMBDA EXPLANATION:
# Lambda works as an anonymous function, and is used for simple operations.
# In this example, we have a function (myfunc) that requires an argument (n), and everything it does is return
# the lambda function a : a * n.
# The functions mydoubler and mytripler calls myfunc, giving the arguments 2 and 3.
# What it does, is change the n value with 2 or 3, and when those functions are called, the given number (11) is a
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



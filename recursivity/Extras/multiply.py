def multiplication(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1+multiplication(num1, num2-1)


print(multiplication(15, 3))

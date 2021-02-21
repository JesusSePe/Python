def fibonacci(num):
    if num <= 1:
        return num
    else:
        operation = fibonacci(num-1) + fibonacci(num-2)
        return operation


print(fibonacci(5))

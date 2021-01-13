def multiply(a, *b):
    total = a
    for i in b:
        total *= i
    print(total)


multiply(5, 5, 5)

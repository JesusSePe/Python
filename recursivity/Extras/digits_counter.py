def digits(num):
    if num < 10:
        return 1
    else:
        return 1+digits(num/10)


print(digits(123456789))

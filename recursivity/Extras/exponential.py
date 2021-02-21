def exponential(base, exp):
    if exp == 1:
        return base
    else:
        return base*exponential(base, exp-1)


print(exponential(5, 4))

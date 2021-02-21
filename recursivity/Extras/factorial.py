# 1*2*3*4*5...
def factorial(num, res=1):
    if num == 1:
        return res
    else:
        return factorial(num-1, res*num)


print(factorial(10))

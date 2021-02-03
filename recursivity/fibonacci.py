# Calculate the fibonacci sequence recursively
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return(fibonacci(num-1) + fibonacci(num-2))

iterations = int(input('How many times do you want to iterate? '))
for i in range(0, iterations+1):
    print(fibonacci(i), end="   ")
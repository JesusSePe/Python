def coins_and_bills(amount):
    times = 0
    options = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}
    for i in options:
        while (amount // i) > 0:
            times += 1
            amount -= i
        if times > 0:
            result[i] = times
            times = 0

    for x in result:
        if x > 2:
            print(result[x], x, '€ bills')
        else:
            print(result[x], x, '€ coins')


user_amount = int(input('Enter the amount to divide: '))
coins_and_bills(user_amount)

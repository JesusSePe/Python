"""Exercise 1. Rus multiplication method."""
from math import trunc
from random import randint


def rus(num1, num2):
    if num1 == 1:
        print(num1, "\t\t", num2, "\t\t", num2)
        return num2
    elif num1 % 2 == 0:
        print(num1, "\t\t", num2)
        return rus(trunc(num1 / 2), num2 * 2)
    else:
        print(num1, "\t\t", num2, "\t\t", num2)
        return num2 + rus(trunc(num1 / 2), num2 * 2)


# print("A\t\t", "B\t\t", "SUMS")
# print(rus(3000, 82))


"""Exercise 2. Mathematical curiosity."""


def curiosity(num):
    if num == 11111111:
        print(num**2)
        return
    else:
        print(num**2)
        return curiosity(num * 10 + 1)


# curiosity(1)

"""Exercise 3. Guess the number."""


def guess(num, min=0, max=1000, attempt=1):
    user_guess = int(input("Which number do you think it is? "))
    if num == user_guess:
        print("CORRECT! You guessed the number at the ", attempt, "attempt")
        return
    else:
        if min < user_guess < num:
            print("The number is between", user_guess, "and", max)
            return guess(num, user_guess, max, attempt+1)
        elif num < user_guess < max:
            print("The number is between", min, "and", user_guess)
            return guess(num, min, user_guess, attempt+1)
        else:
            print("The number is between", min, "and", max)
            return guess(num, min, max, attempt+1)


print("A random number between 0 and 1000 will be chosen.")
guess(randint(0, 1001))


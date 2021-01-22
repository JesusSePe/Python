import math


def name_check(name_to_check):
    try:
        if name_to_check.isalpha():
            return True
    except:
        return False


def pwd_check(pwd_to_check):
    conditions = {'letters': False, 'numbers': False, 'uppercase': False, 'lowercase': False}
    correct = 0
    for i in pwd_to_check:
        if i.islower():
            if not conditions['lowercase']:
                conditions['lowercase'] = True
        elif i.isupper():
            if not conditions['uppercase']:
                conditions['uppercase'] = True
        if i.isalnum():
            if i.isalpha():
                if not conditions['letters']:
                    conditions['letters'] = True
            else:
                if not conditions['numbers']:
                    conditions['numbers'] = True
    for i in conditions:
        if conditions[i]:
            correct += 1
    if correct == 4:
        return True
    else:
        return False


def login(users):
    signup = False
    while not signup:
        name = input("Enter your username: ")
        pwd = input("Enter your password: ")
        if name_check(name) == True and pwd_check(pwd) == True:
            try:
                if users[name] == pwd:
                    signup = True
                    print('Access granted. Welcome', name)
                else:
                    print('Error: User and/or password wrong')
            except:
                print('User or password wrong')
        else:
            print('User or Password not valid.')


def squared_root(num):
    if not num.isnumeric:
        print('That is not a number!')
        return
    try:
        num = int(num)
        print('The square root of', num, ' is', math.sqrt(num))
    except:
        print('This number does not have a squared root')
    return


def divider(num1, num2):
    if not num1.isnumeric:
        print(num1, ' is not a number!')
        return
    if not num2.isnumeric:
        print(num2, ' is not a number!')
        return
    if num2 == 0:
        print('Undefined.')
        return
    try:
        num1 = int(num1)
        num2 = int(num2)
        print('The division of', num1, ' and', num2, ' is:', num1 / num2)
    except:
        print('The division is not possible.')


def minus_hundred(num):
    try:
        if int(num) < 100:
            print("The number must be equal or bigger than 100!")
            return
        num = int(num)
        print("The result is: ", num - 100)
    except:
        print("That's not a number dude, don't bluff me")
    return


def menu():
    run = True
    while run:
        txt = "####################### \n" \
              "### CALCULATOR MENU ### \n" \
              "####################### \n" \
              "1.- Square root\n" \
              "2.- Division\n" \
              "3.- Minus 100\n" \
              "4.- Exit\n"
        print(txt)
        optn = input("Enter an option: ")
        if optn == "1":
            number = input("Enter a number to know its square root: ")
            squared_root(number)
        elif optn == "2":
            number1 = input("Enter a number: ")
            number2 = input("Enter the divisor: ")
            divider(number1, number2)
        elif optn == "3":
            number0 = input("Enter a number: ")
            minus_hundred(number0)
        elif optn == "4":
            run = False
        else:
            print("That option is not valid.")


users_db = {'admin': 'NotSoAdm1n', 'user': 'Ml3m', 'NotInLove': 'JustAL1ttleDrunkOnYou'}
login(users_db)
menu()

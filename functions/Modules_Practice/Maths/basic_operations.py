def add(num1, num2):
    try:
        int(num1)
        int(num2)
        return num1 + num2
    except:
        return 'Please, enter numbers, not letters.'


def subtract(num1, num2):
    try:
        int(num1)
        int(num2)
        return num1 - num2
    except:
        return 'Please, enter numbers, not letters.'


def multiply(num1, num2):
    try:
        int(num1)
        int(num2)
        return num1 * num2
    except:
        return 'Please, enter numbers, not letters.'


def divide(num1, num2):
    try:
        int(num1)
        int(num2)
        return num1 / num2
    except ZeroDivisionError:
        return 'ERROR: Not possible to divide by zero.'
    except:
        return 'Please, enter numbers, not letters.'

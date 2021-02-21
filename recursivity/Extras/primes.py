def prime_check(number, check=2):
    if 0 <= number < 2:
        return True
    if check == number:
        return True
    else:
        if number%check == 0:
            return False
        else:
            return prime_check(number, check+1)


print(prime_check(5))
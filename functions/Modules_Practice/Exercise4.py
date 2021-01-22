# Create a module to verify passwords.
# Conditions:
# Length: minimum 8 characters.
# Uppercase, lowercase, numbers and at least, 1 non-alphanumeric character.
# Password can not contain spaces.
# Return 'The password is not secure' when the password is correct.
# If everything is correct, return True.

def password_check(pwd):
    checks = {'upper': 0, 'lower': 0, 'no_alpha': 0, 'number': 0}
    if len(pwd) < 8:
        return 'Password is too short. Must be 8 characters or longer.'
    for i in pwd:
        if i.isspace():
            return 'Password can not contain spaces!'
        if i.isalnum():
            if i.isalpha():
                if i.islower() and checks['lower'] == 0:
                    checks['lower'] = 1
                elif i.isupper() and checks['upper'] == 0:
                    checks['upper'] = 1
            if i.isdecimal() and checks['number'] == 0:
                checks['number'] = 1
        elif checks['no_alpha'] == 0:
            checks['no_alpha'] = 1
    counter = 0
    for element in checks:
        if checks[element] == 1:
            counter += 1
    if counter == 4:
        return True
    else:
        return 'The password is not secure'

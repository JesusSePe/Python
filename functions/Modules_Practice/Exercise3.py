# Create a module to verify usernames.
# Conditions:
# Length: minimum 6, maximum 12.
# Alphanumeric (numbers and letters).
# Return different messages when the username is too short or too long.
# Return a message when the username has non-alphanumeric characters.
# If everything is correct, return True.

def username_check(username):
    if username.isalnum():
        if 6 <= len(username):
            if 12 >= len(username):
                return True
            else:
                return 'Username can not be longer than 12 characters.'
        else:
            return 'Username can not be shorter than 6 characters.'
    else:
        return 'Username can only have letters and numbers'

# This function returns true if all letters in a word are in alphabetical order.
def alphabetical(word):
    value = 0
    for character in word:
        letter = character.lower()
        if ord(letter) < value:
            return False
        value = ord(letter)
    return True


user_word = input('Type a word: ')
print(alphabetical(user_word))

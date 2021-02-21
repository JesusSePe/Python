def reverser(original, reverse=''):
    if len(original) == len(reverse):
        return reverse
    else:
        return reverser(original, reverse+original[-(len(reverse)+1)])


print(reverser('Hayo sexy Doggy uwu'))

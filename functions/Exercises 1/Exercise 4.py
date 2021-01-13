def concat_n_times(string, times):
    result = ''
    for i in range(0, times):
        result = result + string
    print(result)
    return


user_input = input('Type the string to repeat: ')
user_n = int(input('Enter the amount of times to repeat: '))
concat_n_times(user_input, user_n)

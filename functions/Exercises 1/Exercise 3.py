def three_lines():
    print('/n/n/n')
    return


def nine_lines():
    for i in range(0, 3):
        three_lines()
    return


def clean_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    print('/n')


clean_screen()

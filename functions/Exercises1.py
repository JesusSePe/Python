# This function returns true if all letters in a word are in alphabetical order.
def alphabetical(word):
    value = 0
    for character in word:
        letter = character.lower()
        if ord(letter) < value:
            return False
        value = ord(letter)
    return True


def common(list1, list2):
    list1 = list(dict.fromkeys(list1))
    list2 = list(dict.fromkeys(list2))
    common_items = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_items.append(item1)
    return common_items


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


def concat_n_times(string, times):
    result = ''
    for i in range(0, times):
        result = result + string
    print(result)
    return


def coins_and_bills(amount):
    times = 0
    options = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}
    for i in options:
        while (amount // i) > 0:
            times += 1
            amount -= i
        if times > 0:
            result[i] = times
            times = 0

    for x in result:
        if x > 2:
            print(result[x], x, '€ bills')
        else:
            print(result[x], x, '€ coins')


def pass_students(students, grades):
    students_pass = {}
    for position in range(len(students)):
        if grades[position] >= 5:
            students_pass[students[position]] = grades[position]
    for student in students_pass:
        print(student, students_pass[student])


def amount_pass_students(list_students, list_grades):
    students_dictionary = {}
    for x in range(len(list_grades)):
        if list_grades[x] >= 5:
            students_dictionary[list_students[x]] = list_grades[x]

    print('There are ', len(students_dictionary), 'who passed')


leave_menu = False
while not leave_menu:
    students_list = ['Pere', 'Pau', 'Anna', 'Andrea', 'Pol', 'Nil', 'Montserrat', 'Gerard']
    grades_list = [4.3, 5.6, 5.9, 9.7, 2.6, 6.8, 8.8, 2.4]
    txt = "1.- CHECK IF A WORD IS ALPHABETICAL\n" \
          "2.- RETURN COMMON ITEMS IN 2 LISTS\n" \
          "3.- CLEAN SCREEN\n" \
          "4.- CONCAT STRINGS N TIMES\n" \
          "5.- DIVIDE N MONEY IN BILLS AND COINS\n"
    print(txt)
    option = int(input('CHOOSE AN OPTION: '))
    if option == 1:
        user_word = input('Type a word: ')
        print(alphabetical(user_word))
        input('Press enter key to continue')

    elif option == 2:
        first_list = [1, 2, 1]
        second_list = [2, 3, 1, 4]
        print(common(first_list, second_list))
        input('Press enter key to continue')

    elif option == 3:
        clean_screen()

    elif option == 4:
        user_input = input('Type the string to repeat: ')
        user_n = int(input('Enter the amount of times to repeat: '))
        concat_n_times(user_input, user_n)
        input('Press enter key to continue')

    elif option == 5:
        user_amount = int(input('Enter the amount to divide: '))
        coins_and_bills(user_amount)
        input('Press enter key to continue')

    elif option == 6:
        pass_students(students_list, grades_list)
        input('Press enter key to continue')

    elif option == 7:
        amount_pass_students(students_list, grades_list)
        input('Press enter key to continue')

    else:
        leave_menu = True
        break

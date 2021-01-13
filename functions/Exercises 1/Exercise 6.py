def menu():
    txt = "1.- GRADES STUDENTS WHO PASSED \n" \
          "2.- AMOUNT STUDENTS WHO PASSED \n" \
          "3.- MAX STUDENT GRADE \n" \
          "4.- STUDENTS OVER AVERAGE GRADE \n" \
          "5.- STUDENT GRADE\n" \
          "6.- SORT GRADES FROM BEST TO WORST\n" \
          "7.- EXIT"
    print(txt)
    option_selected = int(input('CHOOSE AN OPTION: '))
    if 0 < option_selected < 8:
        return option_selected
    else:
        return menu()


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


def max_grade(students, grades):
    maximum = max(grades)
    for position in range(len(grades)):
        if grades[position] == maximum:
            print(students[position], grades[position])


def students_average(students, grades):
    average = 0
    for i in grades:
        average += i
    average /= len(grades)
    print('The average grade is:', average)
    for position in range(len(grades)):
        if grades[position] >= average:
            print(students[position], grades[position])


def student_grade(students, grades, student):
    student = student.lower()
    for position in range(len(grades)):
        if students[position].lower() == student:
            return grades[position]
    return None


def order_students_grades(students, grades):
    # Bubble sort
    for x in range(len(grades)-1):
        for i in range(len(grades)-1-x):
            if grades[i] < grades[i + 1]:
                grades[i], grades[i + 1] = grades[i + 1], grades[i]
                students[i], students[i + 1] = students[i + 1], students[i]
    for position in range(len(students)):
        print(students[position], '->', grades[position])


run_program = True
while run_program:
    students_list = ['Pere', 'Pau', 'Anna', 'Andrea', 'Pol', 'Nil', 'Montserrat', 'Gerard']
    grades_list = [4.3, 5.6, 5.9, 9.7, 2.6, 6.8, 8.8, 2.4]
    option = menu()
    if option == 1:
        pass_students(students_list, grades_list)
        input('Press enter key to continue')

    elif option == 2:
        amount_pass_students(students_list, grades_list)
        input('Press enter key to continue')

    elif option == 3:
        max_grade(students_list, grades_list)
        input('Press enter key to continue')

    elif option == 4:
        students_average(students_list, grades_list)
        input('Press enter key to continue')

    elif option == 5:
        student_name = input('Student name: ')
        print(student_grade(students_list, grades_list, student_name))
        input('Press enter key to continue')

    elif option == 6:
        order_students_grades(students_list, grades_list)
        input('Press enter key to continue')

    else:
        run_program = False
        print('PROGRAM ENDED')

# This program has several functions, that are really simple programs.

#########################
# FUNCTIONS DECLARATION #
#########################

# Function to calculate the final price when a discount is applied.
def discounted_price(original, percent):
    return original - (original * percent / 100)


# Function to read numbers. Only does that, ask the user for a number and read it.
def read0to10():
    num = float(input("Enter a number between 0 and 10: "))
    print("The chosen number is...", num, "!")
    return num


# Function to check if a given letter is a vowel or no.
def vowel_check(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel = False
    maybe_vowel = character.lower()
    for i in vowels:
        if i == maybe_vowel:
            vowel = True
    return vowel


# Function to multiply numbers in a list
def multiplier(num_list):
    result = 1
    for i in num_list:
        result = result * i
    return result


# Function that creates multiple histograms given a list
def histogram(numbers_to_multiply):
    for i in numbers_to_multiply:
        print(i * '*')


def words_filter(words_list, minimum_length):
    print('The chosen words are: \n')
    for word in words_list:
        if len(word) > minimum_length:
            print('- ', word)


def uppercase_counter(string):
    counter = 0
    for character in string:
        if character.isupper():
            counter += 1
    print('There are', counter, 'uppercase letters.')


####################
#   MAIN PROGRAM   #
####################

flag_menu = False

while not flag_menu:
    print(
        "1.-EXERCISE 1. FINAL PRICE WITH DISCOUNT\n2.-EXERCISE 2. NUMBER 0-10\n3.-EXERCISE 3. VOWEL OR NOT\n"
        "4.-EXERCISE 4. LIST NUMBERS MULTIPLICATION\n5.-EXERCISE 5. HISTOGRAM\n"
        "6.-EXERCISE 6. WORDS IN ARRAY LONGER OR EQUAL THAN X\n7.-EXERCISE 7. UPPERCASE COUNTER\n"
        "8.-EXIT\nCHOOSE AN OPTION:")
    option = int(input())
    if option == 1:
        # Define and program a function that, given a price and a discount, returns the final price with discount.
        # The function has two parameters: Price, and percent. Returns final price.

        print("EXERCISE 1.")

        discount = 30
        price = float(input("Enter the price: "))
        print("Final price is: ", discounted_price(price, discount))

    elif option == 2:
        # Create a function "read0to10" that asks the user for a number between 0 and 10. If the given number is lower
        # or higher, the program keeps asking for a new one.
        # The function has no parameters, and returns the number given by the user.

        print("EXERCISE 2")

        between = False
        while not between:
            number = read0to10()
            if 0 <= number <= 10:
                between = True
                print("That's between 0 and 10!")
            else:
                print("That's not between 0 and 10.")

    elif option == 3:
        # Write a function that given a character, returns if it's a vowel or no. The return format is True/False

        print('EXERCISE 3')

        letter = input('Please, enter a letter: ')
        print(vowel_check(letter))

    elif option == 4:
        # Write a function that multiplies all elements in a list. Example: [1,2,3,4] should return 24

        print("EXERCISE 4")

        num1 = int(input('Please, enter a number: '))
        num2 = int(input('Please, enter a second number: '))
        num3 = int(input('Please, enter a third number: '))
        num4 = int(input('Please, enter a fourth number: '))
        nums = [num1, num2, num3, num4]
        print('The result of multiplying all the numbers is: ', multiplier(nums))

    elif option == 5:
        # Write a program that has a function named "histogram".
        # This function will get elements from a list of integer numbers and print an histogram in screen using *.

        print("EXERCISE 4")

        nums_to_multiply = [1, 3, 5, 7, 5, 3, 1]
        histogram(nums_to_multiply)

    elif option == 6:
        # Write a program that has a function named words_filter, that gets an array with words, an integer number and
        # returns those words longer than n characters.

        print("EXERCISE 5")

        words = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'nunc', 'mi', 'lectus',
                 'suscipit', 'non', 'bibendum', 'et', 'fringilla', 'ut', 'arcu', 'sed']
        limit = int(input('Enter the minimum length: '))
        words_filter(words, limit)

    elif option == 7:
        # Write a function that asks the user for a string, and tells how many uppercase characters are there.

        print("EXERCISE 6")

        phrase = input('Enter a phrase: ')
        uppercase_counter(phrase)

    else:
        flag_menu = True
        print("PROGRAM ENDED")

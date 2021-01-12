
flag_menu=False

# Function to calculate the final price when a discount is applied.
def DiscountedPrice(price, discount):

    return price - (price * discount / 100)

# Function to read numbers. Only does that, ask the user for a number and read it.
def Read0To10():
    num = float(input("Enter a number between 0 and 10: "))
    print("The choosen number is...", num, "!")
    return num

# Function to check if a given letter is a vowel or no.
def vowelCheck(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel = False
    MaybeVowel = letter.lower()
    for i in vowels:
        if i == MaybeVowel:
            vowel = True
    return vowel

# Function to multiply numbers in a list
def multiplier(nums):
    result = 1
    for i in nums:
        result = result * i
    return result

#Function that creates multiple histograms given a list
def histogram(list):
    for number in list:
        print(number*'*')

def minLength(words, limit):
    print('The choosen words are: \n')
    for word in words:
        if len(word) >= limit:
            print('- ', word)

def UppercaseCounter(phrase):
    counter = 0
    for letter in phrase:
        if letter.isupper() == True:
            counter += 1
    print('There are', counter, 'uppercase letters.')

while not flag_menu:
    print("1.-EXERCISE 1\n2.-EXERCISE 2\n3.-EXERCISE 3\n4.-EXERCISE 4\n5.-EXERCISE 5\n6.-EXERCISE 6\n7.-EXERCISE 7\n8.-EXIT\nCHOOSE AN OPTION:")
    option=int(input())
    if option==1:
       # Definiu i programeu una funció que, donats un preu i un percentatge de descompte, ens torni el preu amb
       # el descompte aplicat. La funció té dos paràmetres: preu i percentatge. Retorna el preu amb el descompte
       # aplicat.
        print("EXERCISE 1")
        discount = 30
        price = float(input("Enter the price: "))
        print("Final price is: ", DiscountedPrice(price, discount))

    elif option==2:
        # Creeu una funció "llegeix1a10" que s'encarregui de demanar a l'usuari que introdueixi pel teclat un nombre
        # entre 0 i 10. Fins que el nombre no està entre el 0 i el 10, continua demanant a l'usuari el número.
        # La funció no tè paràmetres, i retorna un nombre sencer, que és el que s'ha llegit a la funció.
        print("EXERCISE 2")

        exit = False
        while not exit:
            number = Read0To10()
            if number >= 0 and number <=10:
                exit = True
                print("That's between 0 and 10!")
            else:
                print("That's not between 0 and 10.")
    elif option == 3:
        # Escriure una funció que donat un caràcter retorni True si és una vocal, en cas contrari, torna False.
        print('EXERCISE 3')
        letter = input('Please, enter a letter: ')
        print(vowelCheck(letter))
    elif option == 4:
        # Escriure una funció multipliquin els elements d’una llista. Per exemple: multip([1,2,3,4]) hauria de tornar 24.
        num1 = int(input('Please, enter a number: '))
        num2 = int(input('Please, enter a second number: '))
        num3 = int(input('Please, enter a third number: '))
        num4 = int(input('Please, enter a fourth number: '))
        nums = [num1, num2, num3, num4]
        print('The result of multiplying all the numbers is: ', multiplier(nums))
    elif option == 5:
        # Escriure un programa que contingui una funció anomenada histograma, aquesta funció agafarà els elements d’una llista de números sencers i imprimirà un histograma en la pantalla
        list = [1,3,5,7,5,3,1]
        histogram(list)
    elif option == 6:
        # Escriure un programa que contingui una funció anomenada filtra_paraules, que agafi una llista de paraules i un nombre sencer n, i retorni les paraules que tinguin més de n caràcters.
        words = ['lorem','ipsum','dolor','sit','amet','consectetur','adipiscing','elit','nunc','mi','lectus','suscipit','non','bibendum','et','fringilla','ut','arcu','sed']
        limit = int(input('Enter the minimum length: '))
        minLength(words, limit)
    elif option == 7:
        # Escriure una funció que demani a l’usuari que introdueixi una cadena de text i indiqui quantes lletres majúscules té.
        phrase = input('Enter a phrase: ')
        UppercaseCounter(phrase)
    else:
        flag_menu=True
        print("PROGRAM ENDED")


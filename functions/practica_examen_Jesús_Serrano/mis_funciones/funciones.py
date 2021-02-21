
dict_clients = {"34343434A": {"nombre": "Pedro", "telefono": "666994455"},
 "78787878A": {"nombre": "Luis", "telefono": "666765432"},
 "39292939A": {"nombre": "Jose Luis", "telefono": "666232211"}
 }

cliente_compra = {"34343434A": ["AA32E", "AB37Z"], "78787878A": ["CF13U", "KL11T"],
"39292939A": ["ST234"]}

compra_article = {"AA32E": [3,4], "AB37Z": [1,4], "CF13U": [1,1,1,3], "KL11T": [1,3,4],
"ST234": [1,2,3]}

compra_client = {"AA32E": "34343434A", "AB37Z": "34343434A", "CF13U": "78787878A",
"KL11T": "78787878A","ST234": "39292939A"}




# This function creates a menu, and has 2 arguments:
# options: All the options are send as tuples ('Item1', 'Item2', 'Item3', etc)
# Header: By default, header is just a new line.
# To declare a header, it must be done like menu_generator([items on menu], header='MENU')
# Function call example without header: menu_generator('item1', 'item2', 'item3')
# Function call example with header: menu_generator('item1', 'item2', 'item3', header='MAIN MENU')
# The header option MUST be declared always the last one, in case it is declared.
def menus(*tupla, cabecera="\n"):
    flag_menu = False
    while not flag_menu:
        print(cabecera)
        for i in range(len(tupla)):
            print(i + 1, ")", tupla[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(tupla):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")


# This function checks if a personal ID is correct or no.
def peticion_nif():
    valid = False
    while not valid:
        try:
            # First, the program asks the user for it's ID (number + letter)
            nif = input("Please, insert your personal ID here: ")
            if len(nif) == 9:
                # If the length is correct, then the format is checked (8 numbers + letter)
                condition = 0
                # First check. First 8 positions are numbers.
                for i in range(0, 9):
                    if nif[i].isnumeric():
                        condition += 1
                # Secondly, the last position is checked if it's a letter.
                if nif[8].isalpha():
                    condition += 1
                else:
                    print('Last character must be a letter.')
                    condition = 0
                # If all positions are correct, then the ID is shown with uppercase letter.
                if condition == 9:
                    nif_nums = nif[:-1]
                    nif_letter = nif[-1]
                    print(nif_nums, str(nif_letter).upper())
                    valid = True
                else:
                    print('The format is incorrect. Try again with the format 12345678A')
            else:
                print('That ID does not have the correct length. Must have 8 numbers.')
        except:
            print('Unexpected error.')
    for dni in dict_clients:
        if dni == nif:
            return nif

def nuevo_telefono():
    correct = False
    while not correct:
        try:
            # The program tries to save the number as an integer.
            # If there's any letter, then the except will show an error message.
            phone = int(input("Enter your phone number: "))
            # If the length is 9, then the phone number is correct, and it is shown on screen.
            if len(str(phone)) == 9:
                print('The phone is:', phone)
                correct = True
            # In case the length is different to 9, then the phone is not correct, and an error message is shown.
            else:
                print('That phone does not have the correct length. 9 numbers is the correct length.')
        except:
            print('A phone number does NOT HAVE ANY LETTERS!')


def nuevo_nif():
    # First, the customers array is declared with all their IDs (NIF)
    customers = ['34343434A', '75315982K', '28461973W', '73914682L', '74185269B', '16739842M']
    correct = False
    # After declaring all the IDs, then the function asks the user for it's ID, and checks if it's correct or not.
    while not correct:
        try:
            numerodni = int(input('Please, input your nif without letters: '))
            if len(str(numerodni)) == 8:
                correct = True
            else:
                print('NIF MUST HAVE 8 CHARACTERS!')
        except:
            print('WITHOUT LETTERS!')
    # Once the ID has been verified, the function calculates the ID letter using the word array
    # This operation is done by getting the modulus of dividing the ID by 23.
    palabra = 'TRWAGMYFPDXBNJZSQVHLCKE'
    position = numerodni % 23
    # Once the operation is done, the complete ID is saved in a variable, and printed on screen.
    complete = (str(numerodni) + palabra[position])
    print('The complete nif is:', complete)
    # Finally, the function checks if the ID is at the customers array
    for i in customers:
        if i == complete:
            print('This nif already exists in DB')
            return


def nuevo_id_articulo():
    # First, an array with all the products IDs is declared
    dict_items = {0: 12345, 1: 47261, 2: 83424, 3: 84654, 4: 94164, 5: 31254}
    # The function asks the user for a new product ID, and checks if it's valid and inserts it.
    ask = True
    while ask:
        valid = False
        while not valid:
            try:
                new_id = int(input('Enter the product ID: '))
                valid = True
            except ValueError:
                print('The ID must be all numbers.')
        found = False
        # Once the product ID is valid, then the function checks if that ID already exists on the given array.
        for i in range(0, len(dict_items)):
            if new_id == dict_items[i]:
                print('This id is already registered')
                found = True
        if found == False:
            return new_id


def nuevo_stock_artículo():
    # This function asks the user for a new stock amount to the user, and checks if that is correct.
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Enter the amount of stock: '))
            if amount >= 0:
                print('Stock has been updated to', amount)
                valid_input = True
                return amount
            else:
                print('Stock must be 0 or above.')
        except ValueError:
            print('Wrong input. The amount must be a number.')


def nuevo_precio_artículo():
    # This function asks the user for a new product price, and checks if it's correct or not.
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Enter the price: '))
            if amount >= 0:
                print('Price has been updated to', amount)
                valid_input = True
                return amount
            else:
                # In case the user makes any mistake, an error message is given.
                print('Price must be 0 or above.')
        except ValueError:
            print('Wrong input. The price must be an integer number.')


def nuevo_nombre_articulo():
    # This function asks the user for a new item name, and checks if the input is correct.
    dict_items = {0: 'sofa', 1: 'chair', 2: 'wireless charger', 3: 'car charger'}
    cool = False
    while not cool:
        try:
            name = str(input('Enter the item name: '))
            cool = True
        # The input is saved as a string, but if it's not a string an error is given.
        except ValueError:
            print('The name must be a string without numbers.')

    noice = True
    # In case the product name is already on the dictionary, then an error message is given.
    for i in dict_items:
        if dict_items[i] == name:
            print('This item already exists!')
            noice = False
    if noice:
        return
    else:
        nuevo_nombre_articulo()


def imprimir_datos(cabecera, datos, pie="", titulo=""):
    # This function prints a header, data, footer and a title. Last two are optional parameters.
    # In case there's a header, it's printed.
    print(titulo, '\n')
    data_output = ""
    # First, the header is printed.
    for i in cabecera:
        data_output += i
        data_output += '\t' * 5
    print(data_output)
    # After that, a separation is printed using the * character.
    print('*' * len(data_output) * 2)
    # Under the * line, the data is printed in table format.
    for row in range(0, len(datos)):
        data_output = ""
        for items in datos[row]:
            data_output += str(items)
            data_output += '\t' * 5
        print(data_output)
    # Finally, in case there's a footer, then a = line is made, and under it the footer is printed too.
    if pie != "":
        print("=" * len(pie))
        print(pie)


def ordenar_lista(lista, orden):
    # First, we check that all conditions are correct.
    # Orden must be asc or des
    if orden == 'asc' or orden == 'des':
        # The lista variable must be a list.
        if type(lista) == list:
            # The lista variable must have at least, 1 item
            if len(lista) > 0:
                # And finally, all items on the lista list must be the same type.
                items_type = type(lista[0])
                for i in lista:
                    if type(i) != items_type:
                        print('All items on lista must be the same type.')
                        return
            else:
                print('ERROR. List must have at least, 1 item.')
                return
        else:
            print('ERROR. Lista is not a list. Insert a list, please.')
            return
    else:
        print('ERROR. Wrong order parameter given. Must be "asc" or "des".')
        return

    if orden == 'asc':
        lista.sort()
    else:
        lista.sort(reverse=True)


def ordenar_diccionario_por_valor(diccionario, orden, key=""):
    # Check if diciconario is a dictionary
    if type(diccionario) == dict:
        # Check if orden is 'des' or 'asc'
        if orden == 'des' or orden == 'asc':
            # Check if items on diccionario are dictionaries too.
            for item in diccionario:
                if type(diccionario[item]) != dict:
                    print('Items on diccionario must be dictionaries.')
                    return
        else:
            print('orden must be "asc" or "des".')
            return
    else:
        print('diccionario must be a dictionary.')
        return

    # Now, the program checks if the key value has been given or not, and returns the dictionary keys ordered.
    if key == "":
        if orden == 'des':
            dictionary = dict(sorted(diccionario.items(), reverse=True))
        else:
            dictionary = dict(sorted(diccionario.items(), reverse=False))
        print(dictionary.keys())
    else:
        try:
            if orden == 'des':
                dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get(key), reverse=True))
            else:
                dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get(key), reverse=False))
            print(dictionary.keys())

        # In case they given key is not on the dictionary, a invalid key value error is given.
        except:
            print('Invalid key value.')

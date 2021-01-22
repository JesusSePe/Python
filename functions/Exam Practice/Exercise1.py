# This function creates a menu, and has 2 arguments:
# options: All the options are send as tuples ('Item1', 'Item2', 'Item3', etc)
# Header: By default, header is just a new line.
# To declare a header, it must be done like menu_generator([items on menu], header='MENU')
# Function call example without header: menu_generator('item1', 'item2', 'item3')
# Function call example with header: menu_generator('item1', 'item2', 'item3', header='MAIN MENU')
# The header option MUST be declared always the last one, in case it is declared.
def menu_generator(*options, header="\n"):
    flag_menu = False
    while not flag_menu:
        print(header)
        for i in range(len(options)):
            print(i+1, ")", options[i])
        try:
            user_option = int(input("Choose an option: "))
            if 0 < user_option <= len(options):
                flag_menu = True
                return user_option
            else:
                print("Invalid option.")
                flag_menu = False
        except ValueError:
            print("That's no a number. Try again.")


print(menu_generator("List by ID", "List by name", "List by Stock", "Back", header='MAIN MENU'))

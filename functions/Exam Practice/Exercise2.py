# This function checks if a personal ID is correct or no.
def nif_checker():
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
                # If all positions are correct, then the ID is shown with uppercase letter.
                if condition == 9:
                    nif_nums = nif[:-1]
                    nif_letter = nif[-1]
                    print(nif_nums, str(nif_letter).upper())
                else:
                    print('The format is incorrect. Try again with the format 12345678A')

                # print(nif)
            else:
                print('That ID does not have the correct length. Must have 8 numbers.')
        except:
            print('Unexpected error.')


nif_checker()

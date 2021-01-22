def new_phone():
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


new_phone()
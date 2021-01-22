def new_item_price():
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Enter the price: '))
            if amount >= 0:
                print('Price has been updated to', amount)
                valid_input = True
            else:
                print('Price must be 0 or above.')
        except ValueError:
            print('Wrong input. The price must be an integer number.')


new_item_price()

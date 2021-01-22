def new_stock_item():
    valid_input = False
    while not valid_input:
        try:
            amount = int(input('Enter the amount of stock: '))
            if amount >= 0:
                print('Stock has been updated to', amount)
                valid_input = True
            else:
                print('Stock must be 0 or above.')
        except ValueError:
            print('Wrong input. The amount must be a number.')


new_stock_item()
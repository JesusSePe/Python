def new_item_name():
    dict_items = {0: 'sofa', 1: 'chair', 2: 'wireless charger', 3: 'car charger'}
    cool = False
    while not cool:
        try:
            name = str(input('Enter the item name: '))
            cool = True
        except ValueError:
            print('The name must be a string without numbers.')

    noice = True
    for i in dict_items:
        if dict_items[i] == name:
            print('This item already exists!')
            noice = False
    if noice:
        return
    else:
        new_item_name()


new_item_name()

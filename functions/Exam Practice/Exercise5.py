def new_article_ID():
    dict_items = {0: 12345, 1: 47261, 2: 83424, 3: 84654, 4: 94164, 5: 31254}
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
        for i in range(0, len(dict_items)):
            if new_id == dict_items[i]:
                print('This id is already registered')
                found = True
        if found == False:
            return


new_article_ID()

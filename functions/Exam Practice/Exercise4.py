def new_nif():
    customers = ['15768246K', '75315982K', '28461973W', '73914682L', '74185269B', '16739842M']
    correct = False
    while not correct:
        try:
            nif = int(input('Please, input your nif without letters: '))
            if len(str(nif)) == 8:
                correct = True
            else:
                print('NIF MUST HAVE 8 CHARACTERS!')
        except:
            print('WITHOUT LETTERS!')

    word = 'TRWAGMYFPDXBNJZSQVHLCKE'
    position = nif % 23
    complete = (str(nif) + word[position])
    print('The complete nif is:', complete)

    for i in customers:
        if i == complete:
            print('This nif already exists in DB')
            return


new_nif()

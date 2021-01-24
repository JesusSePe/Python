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

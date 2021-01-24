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
            dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get("stock"), reverse=True))
        else:
            dictionary = dict(sorted(diccionario.items(), key=lambda item: item[1].get("stock"), reverse=False))
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


ordenar_diccionario_por_valor({
4: { "Nom_article": "article4", "stock": 6, "preu": 152},
2: { "Nom_article": "article2", "stock": 12, "preu": 132},
3: { "Nom_article": "article3", "stock": 9, "preu": 642},
}, 'asc')


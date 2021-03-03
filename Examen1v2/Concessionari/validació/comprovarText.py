def comprovar_text(var):
    cool = False
    while not cool:
        # Si es demana la marca del cotxe, es comproba que el valor introduit sigui només text.
        if var == 'marca':
            marca = input('Introdueix el nom de la marca: ')
            if marca.isalpha():
                return marca
            else:
                print('Marca no vàlida.')

        # Si es demana el model, i aquest es alpha, Ford i/o Renault, retorna aquest model.
        elif var == 'model':
            model = input('Introdueix el nom de model: ')
            if model.isalpha():
                if model == "Ford" or model == "Renault":
                    return model
                else:
                    print("Model no vàlid. Ha de ser Ford o Renault.")
            else:
                print("Model no vàlid. Ha de ser només text")

        # Si es demana el color, i aquest es alpha, i blanc, negre o vermell, retorna aquest color.
        elif var == 'color':
            color = input()
            if color.isalpha():
                if color == "blanc" or color == "negre" or color == "vermell":
                    return color
                else:
                    print("Color no vàlid. Ha de ser blanc, negre o vermell.")
            else:
                print("Color no vàlid. Ha de ser només text")
        else:
            var = input('Qué vols comprobar? [marca/model/color] ')

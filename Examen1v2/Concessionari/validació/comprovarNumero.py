def comprovar_numero(var):
    cool = False
    while not cool:
        # Si es demana la velocitat del cotxe, es comproba que el valor introduit sigui entre 150 i 270.
        if var == 'velocitat':
            try:
                velocitat = int(input('Introdueix la velocitat màxima: '))
                if 150 <= velocitat <= 270:
                    return velocitat
                else:
                    print('La velocitat màxima ha de ser entre 150km/h i 270km/h.')
            except ValueError:
                print("La velocitat ha de ser un número enter")

        # Si es demana el l'any es comprova que aquest sigui major a 2014 i retorna aquest.
        elif var == 'any':
            try:
                any = int(input('Introdueix el any de matriculació: '))
                if any > 2014:
                    return any
                else:
                    print("El any ha de ser major a 2014")
            except ValueError:
                print("El any ha de ser un número enter. Exemple: 2016")

        else:
            var = input('Qué vols comprobar? [velocitat/any] ')

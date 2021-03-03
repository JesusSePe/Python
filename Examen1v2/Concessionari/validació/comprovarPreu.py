def comprovar_preu():
    cool = False
    while not cool:
        try:
            preu = float(input('Introdueix un preu: '))
            if 10000 < preu < 40000:
                return preu
            else:
                print("El preu ha de ser entre 10000€ i 40000€")
        except ValueError:
            print('Preu incorrecte. Torna a provar.')


print(comprovar_preu())
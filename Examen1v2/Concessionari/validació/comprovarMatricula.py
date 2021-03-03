def comprovar_matricula():
    cool = False
    while not cool:
        # Demanem la matrícula al usuari
        matricula = input("Insereix la nova matrícula")
        try:
            #Comprovem la longitut de la matrícula.
            if len(matricula) == 8:
                condition = 0
                # Primera comprovació. Les perimeres 3 posicions son lletres.
                for i in range(0, 3):
                    if matricula[i].isalpha():
                        condition += 1
                # A continuació, comprovem que la posició 4 es un guió
                if matricula[3]=="-":
                    condition += 1
                # Finalment, comprovem que les últimes 4 posicions son números
                for i in range(4, 8):
                    if matricula[i].isnumeric():
                        condition += 1
                # Si totes les condicions son correctes, es mostra la matricula i es retorna.
                if condition == 8:
                    print("La matrícula ", matricula, " es correcta")
                    return matricula
                else:
                    print('Format incorrecte. Torna a provar amb el format ASD-1234')

            else:
                print('Aquesta matrícula no té la longitut correcta. Ha de tenir 8 posicions.')
        except:
            print('Unexpected error.')
def inserir_millonari():
    continuar = "s"
    while continuar == "s":
        nom = input("Ingrese el nombre: ")
        edat = int(input("Ingrese la edat: "))
        empresa = input("Introduzca el nombre de la empresa: ")
        quantitat = int(input("Ingrese la cantidad de acciones: "))
        cod = len(Millonaris)
        Millonaris[cod+1] = [nom, edat, {empresa: quantitat}]
        continuar = input("¿Desea añadir otro millonario?[s/n]?")
    return


def inserir_empresas():
    continuar = "s"
    while continuar == "s":
        nom = input("Ingrese el nombre de la empresa: ")
        precio = int(input("Ingrese el precio de la accion: "))
        accions[nom] = precio
        continuar = input("¿Desea introducir otra empresa?[s/n]?")
    return accions


def mostrar_millonaris():
    millonaris_txt =    "========================= \n" \
                        "    ElS MILLONETIS SON:   \n" \
                        "========================= \n"
    print(millonaris_txt)
    for cod in Millonaris:
        print("Nom: ", Millonaris[cod][0], "\nEdat: ", Millonaris[cod][1], "\nAccions: ")
        for empresa in Millonaris[cod][2]:
            print("->", empresa, ":", Millonaris[cod][2][empresa])
        input("Pressiona enter per veure el següent millonari: ")


def mes_ric():
    richest = []
    total = 0
    for cod in Millonaris:
        for empresa in Millonaris[cod][2]:
            for accio in accions:
                if empresa == accio:
                    total += accions[accio]*Millonaris[cod][2][empresa]
                    break
        if len(richest) == 0:
            richest.append([total, Millonaris[cod][0]])
        if total > richest[0][0]:
            richest.append([total, Millonaris[cod][0]])
            richest.pop(0)
        total = 0
    for cod in Millonaris:
        if Millonaris[cod][0] == richest[0][1]:
            print("Nom: ", Millonaris[cod][0], "\nEdat: ", Millonaris[cod][1], "\nAccions: ")
            for empresa in Millonaris[cod][2]:
                print("->", empresa, ":", Millonaris[cod][2][empresa])


def modificar():
    data = {}
    nom = input("Introdueix el nom del millonari a modificar: ")
    for cod in Millonaris:
        if Millonaris[cod][0].lower() == nom.lower():
            modify_txt = "1. Nom de millonari\n2. Edat de millonari\n3. Eliminar accions."
            print(modify_txt)
            mod_option = int(input("Introdueix una opció: "))
            if mod_option == 1:
                new_name = input("Introdueix el nou nom: ")
                data[cod] = [new_name, Millonaris[cod][1], Millonaris[cod][2]]
            elif mod_option == 2:
                new_age = input("Introdueix la nova edat: ")
                data[cod] = [Millonaris[cod][0], new_age, Millonaris[cod][2]]
            elif mod_option == 3:
                del_accio = input("ATENCIÓ! Aquesta acció eliminará les accions del millonari! (s/n): ")
                if del_accio == 's':
                    data[cod] = [Millonaris[cod][0], Millonaris[cod][1], {}]
    for i in data:
        del Millonaris[i]
        Millonaris[i] = data[i]

def menu():
    txt = "M E N U  P R I N C I P A L \n" \
        "============================ \n" \
        "A.- Introduir un milionari nou des de Teclat. \n" \
        "B.- Introduir la informació d’una empresa. \n" \
        "C.- Mostrar per pantalla la informació de tots els Milionaris. \n" \
        "D.- Mostrar milionari més ric. \n" \
        "E.- Modificar la informació d’un milionari \n" \
        "X.- Sortir del Programa. \n"

    print(txt)
    opcion = input("Introdueix una opció: ")
    opcion = opcion.lower()
    if opcion == 'a':
        inserir_millonari()
        input("Pressiona enter per continuar: ")
    elif opcion == 'b':
        inserir_empresas()
        input("Pressiona enter per continuar: ")
    elif opcion == 'c':
        mostrar_millonaris()
        input("Pressiona enter per continuar: ")
    elif opcion == 'd':
        mes_ric()
        input("Pressiona enter per continuar: ")
    elif opcion == 'e':
        modificar()
        input("Pressiona enter per continuar: ")
    elif opcion == 'x':
        print("PROGRAM ENDED")
        flag_menu = True
        return flag_menu
    else:
        print('Opció no vàlida')


global accions
accions = {'MicroSopa': 2.67, 'AireTel': 1.2, 'AmenizaDos': 0.98, 'IbemePorUvas': 5.3, 'MacChiton': 0.25}

global Millonaris
Millonaris = {1: ['Elon Musk', 49, {'MicroSopa': 1.5}], 2: ['Michael Maska', 30, {'IbemePorUvas': 10}], 3: ['John Miau', 50, {'IbemePorUvas': 2}]}


global flag_menu
flag_menu = False
while not flag_menu:
    flag_menu = menu()

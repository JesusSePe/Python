"""1) Menu: 0.5pts
Es crearà una funció amb el nom menús (tupla, camsalera, titol), que
rebrà dos paràmetres, una de les tuples, amb el contingut d'un dels
menús i una capçalera. Els paràmetres capsalera i títol seran opcional
tenint com a valor per defecte una cadena buida.
La funció ens mostrarà el menú associat a aquesta tupla.
"""


def menu_generator(datos, titol="", capsalera=""):
    flag_menu = False
    while not flag_menu:
        print(titol)
        print(capsalera * 50)
        for i in range(len(datos)):
            print(i + 1, ")", datos[i])
        try:
            user_option = int(input("Escull una opció: "))
            if 0 < user_option <= len(datos):
                flag_menu = True
                return user_option
            else:
                print("Opció no vàlida.")
                flag_menu = False
        except ValueError:
            print("No es un número, torna a provar.")


menu_generator(("Incloure persona en el cens", "Buscar persona en el cens", "Mostrar soldats Hispania", "Visualitzar categoria del cens"))



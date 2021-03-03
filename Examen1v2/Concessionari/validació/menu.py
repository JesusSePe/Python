# Generem el menu depenent de les dades que rebem
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
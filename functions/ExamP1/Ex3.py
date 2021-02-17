censImperi = {
    "AR1": {"nom": "Claudia", "region": "Roma", "edat": 23, "sexe": "I", "categoria": "centurio"},
    "AD3": {"nom": "Maximo", "region": "Hispania", "edat": 30, "sexe": "H", "categoria": "soldat"},
    "AC2": {"nom": "Marco", "region": "Hispania", "edat": 28, "sexe": "H", "categoria": "soldat"},
    "AV6": {"nom": "Julius", "region": "Roma", "edat": 35, "sexe": "H", "categoria": "cesar"},
    "SS5": {"nom": "Augustus", "region": "Hispania", "edat": 21, "sexe": "H", "categoria": "soldat"},
    "WQ6": {"nom": "Eugenia", "region": "Hispania", "edat": 28, "sexe": "D", "categoria": "centurio"},
    "JU8": {"nom": "Anastacia", "region": "Hispania", "edat": 17, "sexe": "I", "categoria": "soldat"},
    "DF5": {"nom": "Aurelia", "region": "Hispania", "edat": 20, "sexe": "D", "categoria": "poble"},
    "BR1": {"nom": "Antistia", "region": "Roma", "edat": 16, "sexe": "D", "categoria": "centurio"},
    "KR9": {"nom": "Apolonia", "region": "Roma", "edat": 25, "sexe": "I", "categoria": "centurio"},
    "KH7": {"nom": "Acucia", "region": "Roma", "edat": 29, "sexe": "D", "categoria": "centurio"},
    "XH4": {"nom": "Titus", "region": "Roma", "edat": 39, "sexe": "I", "categoria": "poble"},
    "KA2": {"nom": "Aurelio", "region": "Roma", "edat": 15, "sexe": "H", "categoria": "poble"},
    "MJ8": {"nom": "Tiberius", "region": "Roma", "edat": 22, "sexe": "H", "categoria": "poble"},
}
def imprimir(cabecera, datos, titulo=""):
    flag_menu = False
    while not flag_menu:
        print(titulo)
        for item in cabecera:
            print(item, "\t"*3)
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


# Buscar persona en el censo


def buscarPersona():
    cool = False
    while not cool:
        found = []
        nom = str(input("Introdueix el nom de la persona: "))
        for persona in censImperi:
            if censImperi[persona]["nom"].startswith(nom):
                found.append(censImperi[persona])
        if len(found) == 0:
            print("Aquesta persona no ha estat censada")
            return
        else:
            imprimir(("NOM", "REGION", "EDAT", "SEXE", "CATEGORIA"), found, titulo="DADES DEMANADES")
            print(found)
            return found

buscarPersona()

import random
# DB
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
categoria = ["soldat", "cesar", "centurio", "poble"]
regio = ["Roma", "Hispania"]

# Incloure persona en el cens.
# Comprovar nom, categoria i la regió.
def enterFrase(to_check, frase="nom"):
    if to_check == "nom" or to_check == "categoria" or to_check == "regio":
        cool = False
        while not cool:
            try:
                if to_check == "nom" and frase != "nom":
                    if frase.isalpha():
                        return frase
                    else:
                        print("El ", to_check, "ha de ser text.")
                        frase = "nom"
                        cool = False
                elif frase != "nom":
                    # Volem evitar entrar a el else si ja tenim una frase.
                    print("")
                else:
                    if to_check == "nom":
                        frase = str(input('Entra el teu nom: '))
                    elif to_check == "categoria":
                        frase = str(input('Entra la categoría: '))
                    else:
                        frase = str(input('Entra la regio: '))
                if frase.isalpha():
                    if to_check == "categoria" and frase in categoria:
                        cool = True
                        return frase
                    elif to_check == "regio" and frase in regio:
                        cool = True
                        return frase
                    elif to_check == "categoria":
                        print("La categoria no es correcta")
                        frase = str(input('Entra la categoría: '))
                    elif to_check == "regio":
                        print("La regio no es correcta")
                        frase = str(input('Entra la regio: '))
                else:
                    print("El nom ha de ser text.")
            except ValueError:
                print('El nom ha de ser de tipus text i sense números.')
    else:
        return "null"


# Demanem un sexe al usuari, i ha de ser I, D o H.
def enterSexe():
    cool = False
    while not cool:
        try:
            sex = str(input("Introdueix el teu sexe: ")).upper()
            if sex == "I" or sex == "H" or sex == "D":
                cool = True
                return sex
            else:
                print("El sexe ha de ser H (home), D (dona) o I (intersexual)")
        except ValueError:
            print('El sexe ha de ser de tipus text i sense números.')


# Demanem una categoria a l'usuari
def enterCategoria():
    cool = False
    while not cool:
        try:
            cat = str(input("Introdueix la categoria: ")).lower()
            if cat in categoria:
                if cat == "cesar":
                    for persona in censImperi:
                        if censImperi[persona]["categoria"] == "cesar":
                            print("No por haver-hi més de un cesar!!!")
                            cool = False
                else:
                    cool = True
                if cool:
                    return cat
            else:
                print("La categoria no es vàlida")
        except ValueError:
            print('La categoría ha de ser de tipus text i sense números.')


# Demanem la edat a l'usuari i la comprovem.
def enterEdat():
    cool = False
    while not cool:
        try:
            edat = int(input("Introdueix la teva edat: "))
            if 0 <= edat <= 100:
                return edat
            else:
                print("La edat ha de ser entre 0 i 100")
                cool = False
        except ValueError:
            print("La edat ha de ser un NUMERO ENTER entre 0 i 100")


# Retornem una força aleatoria entre 50 i 200
def enterForca():
    return random.randint(50, 200)


# Comprovem la id de la persona.
def idPersona():
    cool = False
    while not cool:
        try:
            id = str(input("Introdueix la teva ID: ")).upper()
            if len(id) == 3:
                check = 0
                for caracter in range(0,2):
                    if not id[caracter].isalpha():
                        print("Format incorrecte. El format ha de ser AB1.")
                    else:
                        check += 1
                if not id[2].isnumeric():
                    print("Format incorrecte. El format ha de ser AB1.")
                else:
                    check += 1
                if check == 3:
                    cool = True
                    for persona in censImperi:
                        if persona == id:
                            print("Aquesta ID ja ha estat registrada")
                            cool = False
                if cool:
                    return id
            else:
                print("Format incorrecte. La id han de ser 2 lletres i un numero junts.")
        except ValueError:
            print("La id han de ser dues lletres i un numero junts")


print(enterFrase("categoria", "asd"))
print(enterSexe())
enterCategoria()
enterEdat()
print(enterForca())
print(idPersona())
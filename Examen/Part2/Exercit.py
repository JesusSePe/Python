from Examen.Part1.Ex1 import menu_generator
from Examen.Part1.Ex2 import enterFrase
from Examen.Part1.Ex2 import enterSexe
from Examen.Part1.Ex2 import enterEdat
from lluita import lluita
import random

# Database
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

# Aquesta funció selecciona els candidats que segueixen les condicions demanades per formar exercit.
def choose (cat, sex, age, reg):
    candidatos = []
    for persona in censImperi:
        if (censImperi[persona]["categoria"] == cat and censImperi[persona]["edat"] >= age) and (censImperi[persona]["sexe"] == sex and censImperi[persona]["region"] == reg):
            candidatos.append(censImperi[persona])
        if len(candidatos) == 3:
            return candidatos
    return candidatos

# Aquesta funcio imprimeix les dades del nou exercit i retorna el poder d'aquest.
def imprimir(datos):
    power = 0
    if len(datos) == 0:
        print("NO DATA FOUND")
    else:
        print("NOM\t\tREGION\t\tEDAT\t\tSEXE\t\tCATEGORIA\t\tPODER")
        for i in datos:
            poder = random.randint(50, 200)
            print(i["nom"], "\t", i["region"],"\t", i["edat"],"\t\t", i["sexe"],"\t\t\t", i["categoria"],"\t", poder)
            power += poder
    return power


# Aquesta funcio gestiona la formacio del nou exercit, fent les crides a funcions pertinents i enviant les variables necessaries.
def formarExercit():
    categoria = input("Entra la categoria: ")
    categoria = (enterFrase("categoria", categoria))
    sexe = enterSexe()
    edat = enterEdat()
    Hispania = choose(categoria, sexe, edat, "Hispania")
    Roma = choose(categoria, sexe, edat, "Roma")
    print("EJERCITO DE HISPANIA")
    power1 = imprimir(Hispania)
    print("EJERCITO DE ROMA")
    power2 = imprimir(Roma)
    lluita(power1, power2)

# Cridem al menu i executem la funcio de formar exercit.
optn = menu_generator(("Incloure persona en el cens", "Buscar persona en el cens", "Mostrar soldats Hispania", "Visualitzar categoria del cens", 'Formar exércit i Lluitar'), titol="CENS ROMA", capsalera="_")
if optn == 5:
    formarExercit()
else:
    print("Sense implementar en la segona part. Proba amb la opció 5")


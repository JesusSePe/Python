import validació

# DB
concessionari = [{"marca": "Renault", "model": "Clio", "color": "Blanc", "preu": 16256.00, "matricula": "AZW-3256",
                  "anyMatriculacio": 2015, "velMax": 240},

                 {"marca": "Renault", "model": "Captur", "color": "Negre", "preu": 11877.00, "matricula": "BCD1478",
                  "anyMatriculacio": 2016, "velMax": 220},

                 {"marca": "Renault", "model": "Koleos", "color": "Blanc", "preu": 13185.00, "matricula": "BHG4562",
                  "anyMatriculacio": 2019, "velMax": 210},

                 {"marca": "Renault", "model": "Megane", "color": "Negre", "preu": 17000.00, "matricula": "FDE2587",
                  "anyMatriculacio": 2012, "velMax": 200},

                 {"marca": "Renault", "model": "Clio", "color": "Blanc", "preu": 10256.00, "matricula": "CDA4444",
                  "anyMatriculacio": 2010, "velMax": 230},

                 {"marca": "Renault", "model": "Kadjar", "color": "Negre", "preu": 26856.89, "matricula": "CFG7845",
                  "anyMatriculacio": 2013, "velMax": 270},

                 {"marca": "Ford", "model": "Kuga", "color": "Blanc", "preu": 14587.70, "matricula": "ARD6958",
                  "anyMatriculacio": 2016, "velMax": 200},

                 {"marca": "Ford", "model": "Fiesta", "color": "Vermell", "preu": 14587.70, "matricula": "BCD1234",
                  "anyMatriculacio": 2016, "velMax": 230},

                 {"marca": "Ford", "model": "Focus", "color": "Vermell", "preu": 14587.70, "matricula": "BCD5284",
                  "anyMatriculacio": 2016, "velMax": 190},

                 {"marca": "Ford", "model": "kuga", "color": "Blanc", "preu": 14587.70, "matricula": "ACD4234",
                  "anyMatriculacio": 2016, "velMax": 200},

                 {"marca": "Ford", "model": "Focus", "color": "Vermell", "preu": 14587.70, "matricula": "AAD0234",
                  "anyMatriculacio": 2016, "velMax": 170}]


# comprovarText fa les crides per rebre la marca, model i color del cotxe. Retorna aquestes dades en un diccionari.
def comprovarText():
    marca = validació.comprovarText.comprovar_text("marca")
    model = validació.comprovarText.comprovar_text("model")
    color = validació.comprovarText.comprovar_text("color")
    cotxe = {"marca": marca, "model": model, "color": color}
    return cotxe


# Crida a la funció comprovar_matricula i retorna aquesta.
def comprovarMatricula():
    matricula = validació.comprovarMatricula.comprovar_matricula()
    return matricula


# Crida a la funció comprovar_preu i retorna el preu
def comprovarPreu():
    preu = validació.comprovarPreu.comprovar_preu()
    return preu


# Crida a les funcions que obtenen la velocitat i l'any
def comrpovarNumero():
    velocitat = validació.comprovarNumero.comprovar_numero("velocitat")
    any = validació.comprovarNumero.comprovar_numero("any")
    return velocitat, any


# nouCotxe demana les dades necessaries per crear un nou cotxe.
def nouCotxe():
    cotxe = comprovarText()
    matricula = comprovarMatricula()
    cotxe["matricula"] = matricula
    preu = comprovarPreu()
    cotxe["preu"] = preu
    nums = comrpovarNumero()
    cotxe["anyMatriculacio"] = nums[1]
    cotxe["velMax"] = nums[0]
    concessionari.append(cotxe)


# Imprimeix els cotxes
def imprimir(values, header=""):
    print(header)
    print("MARCA\t\t\tMODEL\t\tCOLOR\t\tPREU\t\t\tMATRICULA\tANY MATRICULACIO\tVELOCITAT MAXIMA")
    print("-"*100)
    for cotxe in values:
        print(cotxe["marca"], "\t\t", cotxe["model"], "\t\t", cotxe["color"], "\t\t", cotxe["preu"], "\t\t", cotxe["matricula"], "\t\t", cotxe["anyMatriculacio"], "\t\t", cotxe["velMax"])


# Fa la crida a imprimir, filtrant els resultats per marca
def mostrarCotxes():
    search = input("Marca a buscar: ")
    results = []
    for cotxe in concessionari:
        if cotxe["marca"] == search:
            results.append(cotxe)
    imprimir(results, header=search)


# Fa la crida a imprimir, mostrant tots els cotxes del concessionari
def mostrarConcessionari():
    imprimir(concessionari, header="CONCESSIONARI")

# Fa la crida  a imprimir, mostrant el cotxe més car.
def majorPreu():
    results = []
    preu = 0
    for cotxe in concessionari:
        if cotxe["preu"] > preu:
            results = []
            results.append(cotxe)
            preu = cotxe["preu"]
    imprimir(results, header="major preu")


def stockMinim():
    stock = {}
    for cotxe in concessionari:
        try:
            if cotxe["marca"] in stock:
                stock[cotxe["marca"]] += 1
            else:
                stock[cotxe["marca"]] = 0
        except KeyError:
            print("Error")
    print(stock)


# Menu
def main_menu():
    leave = False
    while not leave:
        optn = validació.menu.menu_generator(("Afegeix cotxe", "Mostrar cotxes per marca", "Mostrar tots els cotxes", "Major preu", "StockMinim", "Revalorització", "Sortir"))
        if optn == 1:
            nouCotxe()
        elif optn == 2:
            mostrarCotxes()
        elif optn == 3:
            mostrarConcessionari()
        elif optn == 4:
            majorPreu()
        elif optn == 5:
            stockMinim()
        elif optn == 6:
            print("Under construction")
        elif optn == 7:
            leave = True

main_menu()
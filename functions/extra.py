def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def Hexadecimal(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return Hexadecimal(rest) + digits[x]

def Decimaloctal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num
salir = False
opcion = 0
while not salir:
    print ("-------> 1. Decimal a Hexadecimal <--------")
    print ("-------> 2. Decimal a Octal <--------")
    print ("-------> 3. Decimal a Binario <--------")
    print ("0. Salir")
    print ("Elige una opcion")
    opcion = pedirNumeroEntero()
    if opcion == 1:
        print("1. Decimal a Hexadecimal")
        num= int(input("Escrive un numero decimal: "))
        numbers = []
        numbers.append(num)
        print([Hexadecimal(x) for x in numbers])
        #print ([hex(x) for x in numbers])
    elif opcion == 2:
        print("2. Decimal a Octal")
        numero = int(input('Introduce el número a convertir a binario: '))
        octal = Decimaloctal(numero)
        print(f"El decimal {numero} es {octal} en octal")
    elif opcion == 3:
        print("3. Decimal a Binario")
        numero = int(input('Introduce el número a convertir a binario: '))
        binarizar(numero)
    elif opcion == 0:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 10")
print ("Fin")
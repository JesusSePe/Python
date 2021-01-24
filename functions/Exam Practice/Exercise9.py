def imprimir_datos(cabecera, datos, pie="", titulo=""):
    print(titulo, '\n')
    data_output = ""
    for i in cabecera:
        data_output += i
        data_output += '\t' * 5
    print(data_output)
    print('*' * len(data_output) * 2)
    for row in range(0, len(datos)):
        data_output = ""
        for items in datos[row]:
            data_output += str(items)
            data_output += '\t' * 5
        print(data_output)
    if pie != "":
        print("=" * len(pie))
        print(pie)


imprimir_datos(("ID", "Name", "Stock", "Price"), [(1, 'article1', 10, 22), (2, 'article2', 12, 32), (3, 'article3', 9, 42), (4, 'article4', 6, 52)], pie="Total".ljust(68) + "1000".ljust(20))

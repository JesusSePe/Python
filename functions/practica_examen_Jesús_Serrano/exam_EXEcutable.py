#!/usr/bin/env python3
# coding=utf-8
from mis_funciones import funciones

dict_compres = {"AA32E": {"Data": (2020,11,1), "total_compra": 284},
 "AB37Z": {"Data": (2020,11,1), "total_compra": 674},
 "CF13U": {"Data": (2020,11,1), "total_compra": 1698},
 "KL11T": {"Data": (2020,11,1), "total_compra": 806},
 "ST234": {"Data": (2019,12,7), "total_compra": 1296}
 }
dict_articles = {4: {"Nom_article":"Monitor Packard Bell","stock":6,"preu": 152},
 3: {"Nom_article":"Monitor Acer","stock": 12,"preu": 132},
 2: {"Nom_article":"Portatil Toshiba", "stock": 9,"preu": 642},
 1: {"Nom_article":"Portatil Acer","stock": 10,"preu": 522}
 }
tupla_menu02 = ("Buscar Compras", "Listar Compras", "Crear Compra", "Salir")
tupla_menu011 = ("Listar por id","Listar por nombre","Listar por stock","Volver Atras")

flag_run = True
while flag_run:
    option = funciones.menus(tupla_menu02)
    if option == 1:
        funciones.imprimir_datos(('ID', 'Data', 'Total_compra'), (dict_compres))
    elif option == 2:
        flag_run2 = True
        while flag_run2:
            option2 = funciones.menus(tupla_menu011)
            if option2 == 1:
                funciones.ordenar_diccionario_por_valor(dict_articles, 'asc')
            elif option2 == 2:
                funciones.ordenar_diccionario_por_valor(dict_articles, 'asc', key='Nom_article')
            elif option2 == 3:
                funciones.ordenar_diccionario_por_valor(dict_articles, 'asc', key='stock')
            else:
                flag_run2 = False
    elif option == 3:
        nif = funciones.peticion_nif()
        noice = False
        while not noice:
            cant = (input('Introduce la cantidad a comprar: '))
            try:
                if int(cant) > 0:
                    noice = True
            except:
                print('That is not noice. Try again with a number.')



    else:
        flag_run = False



funciones.peticion_nif()
funciones.nuevo_telefono()
funciones.nuevo_nif()
funciones.nuevo_id_articulo()
funciones.nuevo_stock_artículo()
funciones.nuevo_precio_artículo()
funciones.nuevo_nombre_articulo()
funciones.imprimir_datos(("ID", "Nombre", "Stock", "Precio"), [(1, 'articulo1', 10, 22), (2, 'articulo2', 12, 32), (3, 'articulo3', 9, 42), (4, 'articulo4', 6, 52)], titulo = "Articulos ordenados por nombre")
funciones.ordenar_lista([1,3,5,6,2,8,4,10], 'des')
funciones.ordenar_diccionario_por_valor(dict_articles, 'des', 'stock')

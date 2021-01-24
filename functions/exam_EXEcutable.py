from mis_funciones import funciones
# Dict_articles is declared
dict_articles = {
4: { "Nom_article": "article4", "stock": 6, "preu": 152},
2: { "Nom_article": "article2", "stock": 12, "preu": 132},
3: { "Nom_article": "article3", "stock": 9, "preu": 642},
}
# Functinos are called.
funciones.menus("Buscar Compras","Listar Compras","Crear Compra","Menu Principal")
funciones.menus("Listar por id","Listar por nombre","Listar por stock","Volver Atras")
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

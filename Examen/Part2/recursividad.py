def burbujaRecursiva(lista, pasadas = 0, comparaciones = 0):
    try:

        if len(lista) != len(lista[0]):
            raise ValueError

        for listas in range(len(lista) -1):
            if len(lista[listas]) != len(lista[listas + 1]):
                raise ValueError


        if pasadas > len(lista) -1:
            return lista

        if comparaciones > len(lista) -2 -pasadas:
            return burbujaRecursiva(lista, pasadas + 1, 0)

        if lista[comparaciones][-1 -comparaciones] > lista[comparaciones + 1][-2 -comparaciones]:
            lista[comparaciones][-1 -comparaciones], lista[comparaciones + 1][-2 -comparaciones] = lista[comparaciones + 1][-2 -comparaciones], lista[comparaciones][-1 -comparaciones]

        return burbujaRecursiva(lista, pasadas, comparaciones + 1)

    except ValueError:
        print("ERROR: La lista tiene que ser una matriz cuadrada.")

lista = [[99, 4, 3, -1], [-5, 4, -8, 55], [33,-1,-5,-3], [-2, 6, 8, 5]]
m=burbujaRecursiva(lista)
for i in m:
    print(i)

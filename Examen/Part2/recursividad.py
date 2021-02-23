# Funcio recursiva per ordenar en diagonal.
def recursive_bubble(list, iterations, comparisons):
    if iterations > len(list) - 2:
        return list
    if comparisons > len(list[iterations]) - 1:
        return recursive_bubble(list, iterations + 1, 0)
    if comparisons < len(list[iterations]) - 1 and iterations < len(list) - 1:
        if list[iterations][-comparisons] > list[iterations + 1][-comparisons + 1]:
            list[iterations][-comparisons], list[iterations + 1][-comparisons + 1] = list[iterations + 1][-comparisons + 1], list[iterations][-comparisons]
    if comparisons < len(list[iterations])-1 and iterations > 0:
        if list[iterations - 1][comparisons + 1] > list[iterations][comparisons]:
            list[iterations - 1][comparisons + 1], list[iterations][comparisons] = list[iterations][comparisons], list[iterations - 1][comparisons + 1]
    return recursive_bubble(list, iterations, comparisons + 1)


ul = [[99, 4, 3, -1], [-5, 4, -8, 55], [33, -1, -5, -3], [-2, 6, 8, 5]]
print(recursive_bubble(ul, 0, 4))

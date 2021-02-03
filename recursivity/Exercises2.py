"""1.Dissenyeu una funció recursiva tal que, donats dos llistes de números sencers, retorni un
booleà indicant si són iguals, és a dir, si tenen els mateixos valors a les mateixes posicions.

EX: [1,2,3]  i [1,2,3]  retorna True
    [1,2,3]  i [2,1,3]  retorna False"""
def same_check(list1, list2):
    if len(list1) != len(list2):
        return False
    elif len(list1) == 1 and list1[0] == list2[0]:
        return True
    elif list1[0] != list2[0]:
        return False
    else:
        return same_check(list1[1:], list2[1:])


print(same_check([1,2,3],[2,1,3]))

"""2.Donat una llista de números enters ordenada decreixentment, dissenyeu un programa
recursiu que comprovi si el valor d’algun dels elements de la llista coincideix amb el seu
índex."""


def index_value_check(list):
    if len(list) == 0:
        return False
    elif len(list) == list[0]:
        return True
    else:
        return index_value_check(list[1:])


print(index_value_check([0, 5, 9, 5]))
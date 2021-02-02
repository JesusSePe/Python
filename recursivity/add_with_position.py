def addList(list, pos):
    if len(list) == pos+1:
        return list[-1]
    else:
        return list[-1] + addList(list[:-1], pos)


values=[1, 2, 3, 4, 5, 6]
print(addList(values, 3))
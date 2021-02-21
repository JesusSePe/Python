def maximum(list):
    if len(list) == 1:
        return list[0]
    else:
        if list[0] < list[1]:
            return maximum(list[1:])
        else:
            list.remove(list[1])
            return maximum(list)


print(maximum([30, 4, 6, 2, 4, 15, 2]))

def search(list1, list2):
    for i in list2:
        if i == list1[0]:
            return True
    if len(list1) == 1:
        return False
    else:
        return search(list1[1:], list2)


print(search([1, 2, 4], [5, 3, 5]))

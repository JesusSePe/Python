def common(list1, list2):
    list1 = list(dict.fromkeys(list1))
    list2 = list(dict.fromkeys(list2))
    common_items = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_items.append(item1)
    return common_items


first_list = [1, 2, 1]
second_list = [2, 3, 1, 4]
print(common(first_list, second_list))

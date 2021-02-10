# Recursive bubble sort
def recursive_bubble(list, iterations, comparison):
    if iterations > len(list) - 1:
        return list
    if comparison > len(list)-2-iterations:
        return recursive_bubble(list, iterations+1, 0)
    if list[comparison] > list[comparison + 1]:
        list[comparison], list[comparison + 1] = list[comparison + 1], list[comparison]
    return recursive_bubble(list, iterations, comparison + 1)


ul = [1, -2, 2, 77, 4, -3]
print(recursive_bubble(ul, 0, 0))


# Recursive bubble sort with a list of lists


def recursive_bubble_v2(list, iterations, comparisons):
    if iterations > len(list)-1:
        return list
    if comparisons > len(list[iterations])-2:
        return recursive_bubble_v2(list, iterations+1, 0)
    if list[iterations][comparisons] > list[iterations][comparisons + 1]:
        list[iterations][comparisons], list[iterations][comparisons + 1] = list[iterations][comparisons + 1], list[iterations][comparisons]
    return recursive_bubble_v2(list, iterations, comparisons + 1)


ul2 = [[3, 1, 2], [8, 4, 5], [9, -1, 2]]
print(recursive_bubble_v2(ul2, 0, 0))
def recursive_histogram(list):
    if len(list) == 1:
        print("*"*list[-1])
    else:
        print("*" * list[0])
        return recursive_histogram(list[1:])


recursive_histogram([4, 9, 7])

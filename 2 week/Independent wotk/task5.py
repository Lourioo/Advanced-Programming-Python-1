# task 5
arr = [15, 46, 0, 89, 15, 3, 100, 4, 1]


def list_sort(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])

    return lst.sort(reverse=True)


print('Numbers in descending order of their absolute value:', list_sort(arr))
# task 2
arr = [15, 46, 0, 89, 15, 3, 100, 4, 1]


def change(list):
    list[0], list[-1] = list[-1], list[0]
    return list


print('Changed array:', change(arr))
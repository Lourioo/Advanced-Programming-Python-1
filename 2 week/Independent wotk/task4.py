# task 4
arr = [15, 46, 0, 89, 15, 3, 100, 4, 1]


def useless(s):
    maximum = -2147483648
    for i in range(len(s)):
        if s[i] > maximum:
            maximum = s[i]
    return maximum / len(s)


print('Useless number:', useless(arr))
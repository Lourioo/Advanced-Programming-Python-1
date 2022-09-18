# task 13.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

check = True
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            check = False
            print('Duplicate elements:', arr[i])
            print('Indices of duplicate element:', i, 'and', j)

if check is True:
    print('No duplicate elements')

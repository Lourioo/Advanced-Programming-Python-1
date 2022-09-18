# task 1.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

maximum = -2147483648
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

arr.reverse()
print('Reversed array:', arr)
print('Maximum element:', maximum)

# task 4.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

maximum = -2147483648
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
        n = i

print('Maximum element:', maximum)
print('Index of the maximum element:', n)

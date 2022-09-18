# task 12.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

min_odd = 2147483648
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        if arr[i] < min_odd:
            min_odd = arr[i]

print('Minimum odd element:', min_odd)

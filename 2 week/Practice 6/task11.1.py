# task 11.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

max_even = -2147483648
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] > max_even:
            max_even = arr[i]

print('Maximum even element:', max_even)

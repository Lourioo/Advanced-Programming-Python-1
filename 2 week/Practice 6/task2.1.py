# task 2.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

minimum = 2147483648
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
        n = i

print('Minimum element:', minimum)
print('Index of the minimum element:', n)

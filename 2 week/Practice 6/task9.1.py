# task 9.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

min = abs(arr[0])
minID = 0
for i in range(len(arr)):
    if abs(arr[i]) <= min:
        min = abs(arr[i])
        minID = i
print('Absolute minimum element in array:', arr[minID])
arr.reverse()
print('Reverses array: ', arr)

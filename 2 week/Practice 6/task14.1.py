# task 14.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

max = arr[0]
maxID = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        maxID = i

min = arr[0]
minID = 0
for j in range(len(arr)):
    if arr[j] < min:
        min = arr[j]
        minID = j

print('The max value:', max)
print('The min value:', min)
arr[minID] = max
arr[maxID] = min
print('Swapped array:', arr)

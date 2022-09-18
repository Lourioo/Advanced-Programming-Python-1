# task 6.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

arr.sort()
print('Maximum element in array:', arr[len(arr) - 1])

arr.sort(reverse=True)
print('Minimum element in array:', arr[len(arr) - 1])

# task 3.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

for i in range(len(arr)):
    if arr[i] < 15:
        arr[i] = arr[i] * 2
print('Changed array:', arr)

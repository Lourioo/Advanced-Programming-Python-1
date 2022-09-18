# task 10.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

for i in range(len(arr)):
    if arr[i] < 10:
        arr[i] = 0
    elif arr[i] > 20:
        arr[i] = 1
print('Changed array:', arr)

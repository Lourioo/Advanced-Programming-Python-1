# task 11.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

arr2 = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        if arr[i] < 10:
            arr2.append(arr[i])
if not bool(arr2):
    print('There are no even numbers of the original array less than 10')
else:
    print('Even numbers of the original array less than 10:', arr2)

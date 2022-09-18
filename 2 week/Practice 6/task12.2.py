# task 12.2
s1 = input('Enter the first array: ')
arr1 = list(map(int, s1.split()))
s2 = input('Enter the second array: ')
arr2 = list(map(int, s2.split()))

arr2, arr1 = arr1, arr2
print('First array:', arr2)
print('Second array:', arr1)

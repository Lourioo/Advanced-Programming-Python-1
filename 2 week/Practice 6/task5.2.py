# task 5.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

arr = list(dict.fromkeys(arr))
print(arr)

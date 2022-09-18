# task 8.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

sum = 0
product = 1
for i in range(len(arr)):
    sum += arr[i]
    product *= arr[i]

print('Sum:', sum)
print('Product:', product)

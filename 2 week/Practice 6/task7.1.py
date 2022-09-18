# task 7.1
s = input('Enter an array: ')
arr = list(map(int, s.split()))

sum_even = 0
product_odd = 1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        sum_even += arr[i]
    if arr[i] % 2 != 0:
        product_odd *= arr[i]

print('Sum of even numbers:', sum_even)
print('Product of odd numbers:', product_odd)

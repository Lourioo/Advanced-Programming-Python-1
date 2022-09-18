# task 6.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

sum_greater5 = 0
for i in range(len(arr)):
    if arr[i] > 5:
        sum_greater5 += arr[i]

print('The sum of numbers that grater than 5:', sum_greater5)

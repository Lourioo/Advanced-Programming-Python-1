# task 14.2
import statistics


s = input('Enter an array: ')
arr = list(map(int, s.split()))

mean = statistics.mean(arr)

for i in range(len(arr)):
    if arr[i] > mean:
        arr[i] = 1
print('Changed array:', arr)

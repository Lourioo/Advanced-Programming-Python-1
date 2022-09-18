# task 1.2
import statistics

s = input('Enter an array: ')
arr = list(map(int, s.split()))

mean = statistics.mean(arr)

for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = mean
print('Changed array:', arr)

# task 1.2
import statistics


s1 = input('Enter an array: ')
arr1 = list(map(int, s1.split()))
s2 = input('Enter an array: ')
arr2 = list(map(int, s2.split()))
s3 = input('Enter an array: ')
arr3 = list(map(int, s3.split()))

print('Sum of first array is', sum(arr1), 'and mean is', statistics.mean(arr1))
print('Sum of second array is', sum(arr2), 'and mean is', statistics.mean(arr2))
print('Sum of third array is', sum(arr3), 'and mean is', statistics.mean(arr3))
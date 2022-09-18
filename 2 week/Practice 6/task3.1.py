# task 3.1
import itertools

s = input('Enter an array: ')
arr = list(map(int, s.split()))

sum_odd = sum(itertools.islice(arr, 0, len(arr), 2))
print('Entered array:', arr)
print('The sum of elements with odd indices:', sum_odd)

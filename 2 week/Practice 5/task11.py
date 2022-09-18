# task 11
import re

s = input('Enter a string: ')
n = re.findall('[Nn]+', s)
n_len = map(len, n)
print(max(n_len))
print(s.replace('!', '.'))

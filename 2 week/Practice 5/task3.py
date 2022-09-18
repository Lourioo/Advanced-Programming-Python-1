# task 3
i = 0
n = 0
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i] == '.':
        n += 1
print(s.replace('.', ''))
print(n)

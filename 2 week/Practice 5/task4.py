# task 4
i = 0
n = 0
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i] == 'a':
        n += 1
print(s.replace('a', 'o'))
print(n)
print(len(s))

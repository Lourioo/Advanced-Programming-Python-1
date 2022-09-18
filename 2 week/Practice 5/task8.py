# task 8
i = 0
n = 1
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i] == ' ':
        n += 1
    if s[i] == '.':
        break
print(n)

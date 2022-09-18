# task 1
i = 0
n = 0
s = input('Enter a string: ')
if s[0] == 'e' or s[0] == 'E':
    n += 1
for i in range(len(s)):
    if s[i] == ' ':
        if s[i + 1] == 'e' or s[i + 1] == 'E':
            n += 1
print(n)

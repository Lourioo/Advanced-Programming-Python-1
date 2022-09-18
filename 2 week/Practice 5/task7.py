# task 7
s = input('Enter a string: ')
s1 = s[:len(s) // 2]
s2 = s[len(s) // 2:]
print(s1.replace('n', '*') + s2)

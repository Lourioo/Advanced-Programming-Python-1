# task 13
s = input('Enter a string: ')
left = s.find('(')
right = s.find(')')
print(s[left + 1:right])

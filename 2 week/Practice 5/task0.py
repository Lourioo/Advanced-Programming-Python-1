# task 0
string = ''
s = input('Enter a string: ')
for i in range(len(s)):
    if s[i] != ' ':
        string += s[i]


def palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return 'palindrome'
    else:
        return 'is not a Palindrome'


print(palindrome(string))

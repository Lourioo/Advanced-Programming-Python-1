error_upper_case = 'Missing lowercase letters'
error_lower_case = 'Missing uppercase letters'
error_number = 'Missing numbers'
error_symbol = 'Missing symbols'
error_length = 'Incorrect password length'
strong_pswd = 'The password is perfect!!!'

def check_pass (pswd):
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0
    for i in pswd:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        elif i.isdigit():
            number += 1
        elif i == '*' or i == '-' or i == '#':
            symbol += 1

    if upper_case == 0:
        return error_upper_case
    elif lower_case == 0:
        return error_lower_case
    elif number == 0:
        return error_number
    elif symbol == 0:
        return error_symbol
    elif len (pswd) < 8 or len (pswd) > 8:
        return error_length
    else:
        return strong_pswd

a = input('Enter a password: ')
print(check_pass(a))

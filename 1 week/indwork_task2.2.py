n1 = int(input('First number: '))
op = input('Operation: ')
n2 = int(input('Second number: '))
if op == '+':
    S = n1+n2
    print(n1, op, n2,'=', S)
elif op == '-':
    S = n1-n2
    print(n1, op, n2,'=', S)
elif op == '/':
    if n2 != 0:
        S = n1/n2
        print(n1, op, n2,'=', S)
    else:
        print('Cannot be divided by 0')
elif op == '*':
    S = n1*n2
    print(n1, op, n2,'=', S)
#Sepbossynova Laura CS-2120

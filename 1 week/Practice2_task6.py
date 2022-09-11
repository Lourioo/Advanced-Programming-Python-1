import math
#task 6
print('Do you want to find area of a rectangle, triangle or circle?')
x = input('I want to find area of ')
if x=='rectangle':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    S = a*b
    print('Area of rectangle:', S)
elif x=='triangle':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('Area of triangle:', S)
elif x=='circle':
    r = int(input('Enter r: '))
    S = math.pi*r*2
    print('Area of circle:', S)
else:
    print('Please write "rectangle", "triangle" or "circle"')
#Sepbossynova Laura CS-2120

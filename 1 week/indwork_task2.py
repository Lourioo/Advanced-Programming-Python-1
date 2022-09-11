import math
print('The area of which shape do you want to find?')
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
    S = math.pi*r**2
    print('Area of circle:', S)
elif x=='parallelogram':
    h = int(input('Enter h: '))
    b = int(input('Enter b: '))
    S = b*h
    print('Area of parallelogram:', S)
elif x=='trapezoid':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    h = int(input('Enter h: '))
    S = ((a+b)*h)/2
    print('Area of trapezoid:', S)
elif x=='ellipse':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    S = a*b*math.pi
    print('Area of ellipse:', S)
else:
    print('Please write "rectangle", "parallelogram", "trapezoid", "triangle", "circle" or "ellipse"')
#Sepbossynova Laura CS-2120

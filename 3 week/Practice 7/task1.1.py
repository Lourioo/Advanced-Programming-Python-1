# task 1.1
import math

print('Do you want to find area of a rectangle, triangle or circle?')
x = input('I want to find area of ')


def find_area(shape):
    if shape == 'rectangle':
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        s = a * b
        print('Area of rectangle:', s)
    elif shape == 'triangle':
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = int(input('Enter c: '))
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Area of triangle:', s)
    elif shape == 'circle':
        r = int(input('Enter r: '))
        s = math.pi * r * 2
        print('Area of circle:', s)
    else:
        print('Please write "rectangle", "triangle" or "circle"')


find_area(x)

import math
#task 5
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
D = b**2-4*a*c
if D>0:
    x1=(-b-math.sqrt(D))/2*a
    x2=(-b+math.sqrt(D))/2*a
    print('x1 =',x1,'x2 =',x2)
elif D==0:
    x1=(-b-math.sqrt(D))/2*a
    print('x1 = x2 =',x1)
else:
    print('There are no roots')
#Sepbossynova Laura CS-2120

# task 2.2
n = int(input('Enter the number of rows:'))
m = int(input('Enter the number of columns:'))
a = []
print('Enter an array:')
for i in range(n):
    a.append(list(map(int, input().split())))

print('Your array:')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

for i in range(n):
    tmp = a[i][0]
    a[i][0] = a[i][m - 1]
    a[i][m - 1] = tmp

print('Changed array:')
for i in range(n):
    for j in range(m):
        print("%2d " % a[i][j], end=' ')
    print()

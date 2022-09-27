# task 4.2
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

a = [[1 if x > 0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))], '')

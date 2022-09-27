# task 4.1
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

s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print(a[s.index(max(s))], 'largest sum:', max(s), a[s.index(min(s))], 'smallest sum:', min(s))

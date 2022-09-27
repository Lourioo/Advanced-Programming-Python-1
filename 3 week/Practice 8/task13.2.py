# task 13.2
n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))
a = []
print('Enter an array:')
for i in range(n):
    a.append(list(map(int, input().split())))

MIN = min(map(min, a))
MAX = max(map(max, a))
print('Min:', MIN, ', max:', MAX)

a[a.index(MIN)], a[a.index(MAX)] = a[a.index(MAX)], a[a.index(MIN)]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

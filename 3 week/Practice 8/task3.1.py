# task 3.1
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

answer = "YES"
for i in range(m):
    for j in range(n):
        if a[i][j] != a[j][i]:
            answer = "NO"
            break
print(answer)

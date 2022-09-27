# task 5.1
def sortArr(arr, n, m):
    for i in range(n):
        arr[i].sort()
    print()


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

print('Changed array:')
sortArr(a, m, n)

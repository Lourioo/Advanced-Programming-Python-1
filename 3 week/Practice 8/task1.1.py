# task 1.1
n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])

p = 0
s = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            s += a[i][j]
            p += 1

print("Number of positive:", p)
print("Sum:", s)

# task 2.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

pos = []
neg = []
for i in range(len(arr)):
    if arr[i] > 0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])

print('Positive elements:', pos)
print('Other elements:', neg)

# task 10.1
arr = []
for i in range(210, 231):
    arr.append(i)

res = [sub for sub in arr if len(set(str(sub))) == len(str(sub))]

print(str(res))

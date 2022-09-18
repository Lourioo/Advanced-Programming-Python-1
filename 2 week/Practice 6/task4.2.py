# task 4.2
s = input('Enter an array: ')
arr = list(map(int, s.split()))

odd_el = []
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        odd_el.append(arr[i])

for i in range(len(odd_el)):
    j = i + 1
    for j in range(len(odd_el)):
        if odd_el[i] < odd_el[j]:
            temp = odd_el[i]
            odd_el[i] = odd_el[j]
            odd_el[j] = temp

odd_el.reverse()
if not bool(odd_el):
    print('There are no odd elements')
else:
    print('Sorted array with odd elements:', odd_el)

# task 5.2
def allDiv(n):
    for i in range(1, n - 1):
        if n % i == 0:
            print(i, end=" ")


n = int(input("numb: "))
allDiv(n)

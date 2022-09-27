# task 8.1
def divisible(n):
    for i in range(n):
        if allDigitsDivide(i):
            print(i)


def allDigitsDivide(n):
    temp = n
    while temp > 0:

        digit = temp % 10
        if not (digit != 0 and n % digit == 0):
            return False

        temp = temp // 10

    return True


n = int(input("enter the numb: "))
divisible(n)

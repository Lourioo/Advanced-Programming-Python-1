class calculator:
    def add(x1, x2):
        return x1 + x2

    def subtract(x1, x2):
        return x1 - x2

    def multiply(x1, x2):
        return x1 * x2

    def divide(x1, x2):
        return x1 / x2


x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
print("Sum:", calculator.add(x, y))
print("Difference:", calculator.subtract(x, y))
print("Multiplication:", calculator.multiply(x, y))
print("Division:", calculator.divide(x, y))

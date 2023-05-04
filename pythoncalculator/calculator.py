def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponent(x, y):
    return x**y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponential")

while True:
    # take input from the user
    operation = input("Select Operation (ex. 1 = Add, 2 = Subtract): ")

    if operation in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        elif operation == "5":
            print(num1, "**", num2, "=", exponent(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")

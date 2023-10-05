def add(a, b):
    return a + b

def divide_number(a, b):
    if b == 0:
        return "Error! Division by 0"
    else:
        return a / b

def calculator():
    operation = input("Enter the operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = add(num1, num2)


    print(f"{result:.0f}")

calculator()

if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /): ")
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")
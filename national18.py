num1 = float(input("Enter number 1: "))
op = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Not allowed to divide by zero")

else:
    print("Invalid operator! Please use +, -, *, or / only.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operator (+, -, *, /): ")
result = None
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:     
            result = num1 / num2
    case _:
        print("Invalid operator.")
if result:
    print(f"The result is {result}")
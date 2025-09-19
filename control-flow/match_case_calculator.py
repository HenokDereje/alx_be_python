number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Choose the operator (+, -, *, /): ")
result = None
match operator:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:     
            result = number1 / number2
if result:
    print(f"The result is {result}")
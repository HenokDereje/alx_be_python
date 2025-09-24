def perform_operation(num1, num2, operation):
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "You cannot divide by Zero!"
        else:
            result = num1 / num2
    return result
def perform_operation(num1, num2, operation):
    result = None
    if operation == "add":
        result = num1 + num2
    if operation == "subtract":
        result = num1 - num2
    if operation == "multiply":
        result = num1 * num2
    if operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            return "You cannot divide by Zero!"
    return result
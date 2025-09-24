def perform_operation(num1, num2, operation):
    result = None
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                return "You cannot divide by Zero!"
    return result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation_type = input("Choose the operation (+, -, *, /): ")


if num2 == 0:
    print("Cannot divide by zero")
    raise SystemExit(1)

match operation_type:
    case "+":
        print(f'The result is {num1 + num2}')
    case "-":
        print(f'The result is {num1 - num2}')
    case "*":
        print(f'The result is {num1 * num2}')
    case "/":
        print(f'The result is {num1 / num2}')
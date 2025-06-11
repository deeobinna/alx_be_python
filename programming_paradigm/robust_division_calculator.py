def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f'The result of the division is {result}'
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

print(safe_divide(12,0))


def convert_to_floats(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return f'The result of the division is {numerator/denominator}'
    except ValueError:
        return "Error: Please enter numeric values only."

print(convert_to_floats(12, 4))
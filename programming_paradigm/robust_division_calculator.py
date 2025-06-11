def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(safe_divide(12,0))


def convert_to_floats(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator/denominator
    except ValueError:
        return "Error: Non-numeric value provided."

print(convert_to_floats(12, 4))
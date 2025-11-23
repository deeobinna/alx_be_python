FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32   

user_input = input("Enter the temperature to convert: ")
user_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if user_temp.upper() == 'C':
    converted_temp = convert_to_fahrenheit(float(user_input))
    print(f"{user_input}°C is {converted_temp:.2f}°F")
elif user_temp.upper() == 'F':
    converted_temp = convert_to_celsius(float(user_input))
    print(f"{user_input}°F is {converted_temp:.2f}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
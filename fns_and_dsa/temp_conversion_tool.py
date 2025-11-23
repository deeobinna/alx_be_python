FAHRENHEIT_TO_CELSIUS = (5.0 / 9.0)
CELSIUS_TO_FAHRENHEIT = (9.0 / 5.0)

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS 

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32   

user_input = input("Enter temperature (e.g., 100F or 37C): ").strip()
if user_input[-1].upper() == 'F':
    fahrenheit = float(user_input[:-1])
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}F is {celsius:.2f}C")

elif user_input[-1].upper() == 'C':
    celsius = float(user_input[:-1])
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f"{celsius}C is {fahrenheit:.2f}F")   

else:
    print("Invalid input. Please enter a temperature ending with 'F' or 'C'.")
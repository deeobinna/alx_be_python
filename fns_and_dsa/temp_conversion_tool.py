FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    input_value  = input('Enter temperature in Fahrenheit (0F): ')
    if not input_value.endswith('F'):
        raise ValueError("Input must end with 'F' for Fahrenheit")
    else:
        return round((float(input_value[:-1]) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR, 2)
    

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    input_value  = input('Enter temperature in Celsius (0C): ')
    if not input_value.endswith('C'):
        raise ValueError("Input must end with 'C' for Celsius")
    else:
        return round((float(input_value[:-1]) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32, 2)
    


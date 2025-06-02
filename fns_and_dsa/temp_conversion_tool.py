FAHRENHEIT_TO_CELSIUS_FACTOR = None
CELSIUS_TO_FAHRENHEIT_FACTOR = None

temperature_to_convert = input("Enter the temperature to convert (e.g., 100F or 37C): ")
if temperature_to_convert[-1].upper() == 'F':
    
    def convert_to_celcius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        global FAHRENHEIT_TO_CELSIUS_FACTOR
        if FAHRENHEIT_TO_CELSIUS_FACTOR is None:
            FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
        return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
elif temperature_to_convert[-1].upper() == 'C':
    def convert_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        global CELSIUS_TO_FAHRENHEIT_FACTOR
        if CELSIUS_TO_FAHRENHEIT_FACTOR is None:
            CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
else:
    raise ValueError("Invalid temperature format. Please use 'F' for Fahrenheit or 'C' for Celsius.")   
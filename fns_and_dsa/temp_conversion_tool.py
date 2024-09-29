# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # This line is explicitly included as required

def convert_to_celsius(fahrenheit):
    """
    Converts a given temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): The temperature in Fahrenheit.
    
    Returns:
        float: The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a given temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): The temperature in Celsius.
    
    Returns:
        float: The temperature converted to Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Get the temperature input from the user
        temperature = float(input("Enter the temperature to convert: "))

        # Get the unit of the temperature input from the user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Invalid unit entered
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Invalid temperature entered (not a number)
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

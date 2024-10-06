def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors.

    Args:
        numerator (str): The dividend.
        denominator (str): The divisor.

    Returns:
        str: The result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError
        result = num / denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
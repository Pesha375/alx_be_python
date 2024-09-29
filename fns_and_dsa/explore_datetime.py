from datetime import datetime, timedelta

def display_current_datetime():
    """
    Function to display the current date and time in a readable format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as a string
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """
    Function to calculate the future date by adding the specified number of days to the current date.
    
    Args:
        days (int): Number of days to add to the current date.
    """
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date as YYYY-MM-DD
    print(f"Future date: {formatted_future_date}")

def main():
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

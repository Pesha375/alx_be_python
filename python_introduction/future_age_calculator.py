# Prompting the user to input their current age
current_age = int(input("How old are you? "))

# Calculating the user's age in 2050
future_year = 2050
current_year = 2023
years_to_future = future_year - current_year
age_in_2050 = current_age + years_to_future

# Printing the result
print(f"In 2050, you will be {age_in_2050} years old.")
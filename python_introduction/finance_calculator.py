# Prompting the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projecting annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)

# Displaying the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        print("Invalid priority level")
        exit()

if time_bound.lower() == "yes":
    urgency_message = "that requires immediate attention today!"
else:
    urgency_message = "Consider completing it when you have free time."

# Provide a Customized Reminder
if time_bound.lower() == "yes":
    print(f"Reminder: '{task}' is a {priority_message} task {urgency_message}")
else:
    print(f"Note: '{task}' is a {priority_message} task. {urgency_message}")
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is is time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "no": 
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
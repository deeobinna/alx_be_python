task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "low": 
        if time_bound == "no":
            print(f"Note: {task} is a low proirity task. Conside completing it when you have free time.")
    case _:
        print(f"Reminder: Don't forget to complete your task: {task}.")
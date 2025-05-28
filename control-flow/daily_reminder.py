task = input("Enter a task description: ")
priority = input("Enter task priority (high/medium/low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f'Reminder: {task} is a high priority task that requires immediate attention today!')
    case "low":
        if time_bound == "no":
            print(f'Note: {task} is a low priority task. Consider completing it when you have free time.')
        
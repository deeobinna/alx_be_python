Task = input("Enter a task description: ")
Priority = input("Enter task priority (high/medium/low): ").strip().lower()
Time_Bound = input("Is this task time-bound? (yes/no): ").strip().lower()

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f'Reminder: {Task} is a high priority task that requires immediate attention today!')
    case "low":
        if Time_Bound == "no":
            print(f'Note: {Task} is a low priority task. Consider completing it when you have free time.')
        
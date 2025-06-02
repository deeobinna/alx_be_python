def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now() # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")


number_of_days = int(input("Enter the number of days to add: "))
def calculate_future_date(days):
    from datetime import datetime, timedelta
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days)  # Add the specified number of days
    print(f"New date after adding {days} days: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")
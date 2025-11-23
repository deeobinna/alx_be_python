#Research how to use the datetime module to obtain the current date and time.
#Create a function with a name display_current_datetime and
#save the current date inside a current_date variable
#Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.```python

from datetime import datetime

def display_current_datetime():
    # Obtain the current date and time
    now = datetime.now()
    
    # Save the current date inside a variable
    current_date = now.date()
    
    # Format the current date and time
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current Date: {current_date}")
    print(f"Current Date and Time: {formatted_datetime}")




def calculate_future_date(days):
    # Obtain the current date
    now = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = now + timedelta(days=days)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"Future Date after {days} days: {formatted_future_date}")
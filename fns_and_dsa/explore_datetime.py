from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    current_date = display_current_datetime()
    print("Current date and time:", current_date)
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    days_time = timedelta(days=number_of_days)
    future_date = current_date + days_time
    print("Future date:", future_date)

calculate_future_date()

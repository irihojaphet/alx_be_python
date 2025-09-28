# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # save current date and time
    current_date = datetime.now()
    # format and print
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # save future date
    future_date = datetime.now() + timedelta(days=days)
    # format and print
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: show current date and time
    display_current_datetime()
    
    # Part 2: prompt for days and calculate
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

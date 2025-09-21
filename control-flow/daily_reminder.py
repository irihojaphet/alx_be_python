# A Python script that provides customized task reminders using control flow statements

def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    
    # Process the task based on priority using Match Case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Make sure to complete it today.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a medium priority task. Try to complete it within the next few days.")
        
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        case _:
            print("Invalid priority level. Please use high, medium, or low.")
            return
    
    # Additional loop to ask if user wants to set another reminder
    while True:
        another = input("\nWould you like to set another reminder? (yes/no): ").lower().strip()
        if another == "yes":
            print("\n" + "="*50)
            main()  # Recursive call to start over
            break
        elif another == "no":
            print("Have a productive day!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Run the program
if __name__ == "__main__":
    print("=== Daily Task Reminder ===")
    main()
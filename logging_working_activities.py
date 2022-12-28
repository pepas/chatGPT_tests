import os

# Create a list to store the activities
activities = []

def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def add_activity():
    """Add a new activity to the list."""
    start = input("Enter start time: ")
    end = input("Enter end time: ")
    description = input("Enter description: ")
    activities.append({"start": start, "end": end, "description": description})

def delete_activity():
    """Delete an activity from the list."""
    index = int(input("Enter the index of the activity to delete: "))
    del activities[index]

def get_activity_summary():
    """Get a summary of the activities."""
    summary = ""
    for i, activity in enumerate(activities):
        summary += f"{i}: {activity['start']} - {activity['end']}: {activity['description']}\n"
    return summary

def display_menu():
    """Display the main menu."""
    clear_screen()
    print("Work Log\n")
    print("1. Add activity")
    print("2. Delete activity")
    print("3. View activities")
    print("4. Quit")

def main():
    """Main function of the app."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_activity()
        elif choice == "2":
            delete_activity()
        elif choice == "3":
            clear_screen()
            print(get_activity_summary())
            input("\nPress enter to continue...")
        elif choice == "4":
            break

# Run the main function
if __name__ == "__main__":
    main()
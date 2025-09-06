# Import datetime so we can timestamp diary entries
from datetime import datetime


def write_entry():
    """Allows the user to write a new diary entry."""
    # Ask the user to start typing their entry
    entry_text = input("Enter your diary entry (type 'DONE' on a new line to finish):\n")

    # We'll collect all lines of the entry in this list
    entry_lines = []

    # Keep asking for more lines until the user types 'DONE'
    while entry_text.strip().upper() != 'DONE':
        entry_lines.append(entry_text)  # save what they typed
        entry_text = input()  # ask for the next line

    # Add a timestamp to the entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the diary file in append mode ("a" means "add to the end")
    with open("diary.txt", "a") as f:
        f.write(f"Date: {timestamp}\n")                # write the date
        f.write("\n".join(entry_lines) + "\n\n---\n\n")  # write the entry + separator

    print("Entry saved.")


def read_entries():
    """Reads and displays all diary entries."""
    try:
        # Try opening the diary file in read mode
        with open("diary.txt", "r") as f:
            content = f.read()  # read everything inside

            if content:  # check if there's anything written
                print("\n--- Your Diary Entries ---\n")
                print(content)
            else:
                print("No entries yet.")  # file exists but empty

    except FileNotFoundError:
        # If the file doesn’t exist yet, we handle the error gracefully
        print("No diary entries found. Start by writing one!")


def main():
    # Infinite loop so the diary menu keeps running until user exits
    while True:
        print("\nDiary Menu:")
        print("1. Write a new entry")
        print("2. Read all entries")
        print("3. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Match their choice to an action
        if choice == '1':
            write_entry()
        elif choice == '2':
            read_entries()
        elif choice == '3':
            print("Exiting diary. Goodbye!")
            break  # break ends the loop → program stops
        else:
            print("Invalid choice. Please try again.")  # invalid input handling


# This ensures the code only runs when executed directly (not imported as a module)
if __name__ == "__main__":
    main()

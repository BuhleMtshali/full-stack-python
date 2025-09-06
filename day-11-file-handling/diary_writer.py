from datetime import datetime

def write_entry():
    """Allows the user to write a new diary entry."""
    entry_text = input("Enter your diary entry (type 'DONE' on a new line to finish):\n")
    entry_lines = []
    while entry_text.strip().upper() != 'DONE':
        entry_lines.append(entry_text)
        entry_text = input()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"Date: {timestamp}\n")
        f.write("\n".join(entry_lines) + "\n\n---\n\n")
    print("Entry saved.")

def read_entries():
    """Reads and displays all diary entries."""
    try:
        with open("diary.txt", "r") as f:
            content = f.read()
            if content:
                print("\n--- Your Diary Entries ---\n")
                print(content)
            else:
                print("No entries yet.")
    except FileNotFoundError:
        print("No diary entries found. Start by writing one!")

def main():
    while True:
        print("\nDiary Menu:")
        print("1. Write a new entry")
        print("2. Read all entries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            write_entry()
        elif choice == '2':
            read_entries()
        elif choice == '3':
            print("Exiting diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
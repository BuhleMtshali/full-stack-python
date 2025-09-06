# importing date
from datetime import datetime

# function for diary entry
def write_entry():
    """Allows the user to enter a new diary entry"""
    entry_text = input("Enter your diary entry (type 'DONE' on a new line to finish): \n")
    entry_lines = []
    while entry_text.strip().upper() != 'DONE':
        entry_lines.append(entry_text)
        entry_text = input()
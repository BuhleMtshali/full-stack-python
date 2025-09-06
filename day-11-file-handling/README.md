## 📓 Diary Writer (File Handling Project)

A simple command-line diary app built with Python.
This project demonstrates file handling (reading & writing), exception handling, and using timestamps for logging entries.


## 🚀 Features

- ✍️ Write Diary Entries

    -  Add new entries line by line until you type DONE.

    - Automatically timestamps each entry.

- 📖 Read Entries

    - View all your past diary entries stored in diary.txt.

- ❌ Handles Missing Files

    - If the diary file doesn’t exist yet, the program won’t crash—it shows a friendly message.

- 🔄 Menu System

    - Simple CLI menu to choose between writing, reading, or exiting.


## 🛠️ Tech Used

- Python 3

- datetime → For generating timestamps.

- File Handling (open, with, read/write modes)

- Exception Handling (try/except)


## 📂 File Structure

```
day-11-file-handling/

│── diary_writer.py   # main program

│── diary.txt         # entries stored here (auto-created if missing)

```


## ▶️ How to Run

1. Clone this repo or copy the script.

2. Run in terminal:

```
python3 diary_writer.py

```

3. Use the menu:

    - Press 1 → Write a new diary entry.

    - Press 2 → Read all previous entries.

    - Press 3 → Exit.


## 📝 Sample Run

```
Diary Menu:
1. Write a new entry
2. Read all entries
3. Exit
Enter your choice: 1
Enter your diary entry (type 'DONE' on a new line to finish):
Had a productive day coding.
DONE
Entry saved.

```


## 🔑 What I Learned

- Using with open() safely to handle files.

- Writing in append mode (a) vs. reading (r).

- Handling missing files with FileNotFoundError.

- Adding timestamps with datetime.

- Creating a simple menu loop for CLI projects.


## 📌 Future Improvements

- 🔒 Password protection for diary.

- 🔍 Search for entries by date or keyword.

- 🌐 Convert to a GUI or web app.
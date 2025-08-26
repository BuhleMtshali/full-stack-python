## 🪨📄✂️ Rock, Paper, Scissors Game


## 📌 Project Overview

This is a simple Rock, Paper, Scissors game built in Python.
The player competes against the computer, which makes random choices.
The program keeps track of wins, losses, and ties, and displays the results after each round.

This project helps practice:

- Loops (while True)

- Conditional statements (if/elif/else)

- Random number generation (random)

- Error handling (e.g., handling invalid input)

- String formatting (f-strings / .format)


## 🛠️ Features

✔️ Play against the computer

✔️ Input validation (no crashing on invalid input)

✔️ Keeps score of Wins, Losses, and Ties

✔️ Option to quit anytime with "q"

✔️ Fun & interactive console messages 🎉


## 🚀 How to Run

1. Clone or download the project.

2. Make sure you have Python 3+ installed.

3. Open your terminal and run

```
python rock_paper_scissors.py

```


## 🎮 Sample Gameplay

```
------ Rock, Paper, Scissors Game ------

0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
> r
Rock versus...
Scissors
You win! 🎉

1 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
> p
Paper versus...
Rock
You win! 🎉

2 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
> q
Thanks for playing! 👋

```


## 📚 What I Learned

- How to use random.choice() to simulate the computer’s move.

- Using loops to keep the game running until the user quits.

- Handling invalid inputs without breaking the game.

- Tracking game statistics (wins, losses, ties).

- Printing results with f-strings for cleaner code.


## 💡 Next Improvements

- Add a best-of-3 or best-of-5 mode.

- Add emoji support (🪨📄✂️) instead of just text.

- Save high scores in a file.

- Create a GUI version using Tkinter or PyQt
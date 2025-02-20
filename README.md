# Rock Paper Scissors Game

## Overview
This is a simple Rock Paper Scissors game built using the `tkinter` library in Python. The game allows the player to choose Rock, Paper, or Scissors, and randomly selects a move for the computer. The result of each match (Player wins, Computer wins, or Draw) is displayed on the screen.

## Features
- Player can choose Rock, Paper, or Scissors using buttons.
- Computer's move is randomly selected.
- The result of each match is displayed.

## Requirements
- Python 3.x
- `tkinter` library (usually included with standard Python installation)

## How to Run
1. Save the provided code in a file, for example `ROCK_PPR_SCISSORS.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `ROCK_PPR_SCISSORS.py` is saved.
4. Run the following command:

```sh
python rps_game.py
```

## Code Explanation

1. **Class Definition:**
   - `RPSGameApp` is a subclass of `tk.Tk` which represents the main application window.

2. **Widgets Creation:**
   - Three buttons (`Rock`, `Paper`, `Scissors`) are created for the player to make a choice.
   - A label is created to display the result of the game.

3. **Player Choice:**
   - The `player_choice` method is called when a player makes a choice. This method randomly selects the computer's move and determines the winner.

4. **Determine Winner:**
   - The `determine_winner` method compares the player's move with the computer's move and determines the result.

5. **Running the Application:**
   - The application is created and run using `app = RPSGameApp()` and `app.mainloop()`.
--->**_Note:_**
The images of required for the framework of game are not included in the file.
You can save any image of ur choice in the respective directory. Also note that the name of images mentioned in the code should also be changed accordingly.

import tkinter as tk
import random

# Define the main application class
class RPSGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Rock Paper Scissors Game')
        self.geometry('300x200')

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Buttons for player choices
        self.rock_button = tk.Button(self, text='Rock', command=lambda: self.player_choice('rock'))
        self.rock_button.pack()

        self.paper_button = tk.Button(self, text='Paper', command=lambda: self.player_choice('paper'))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self, text='Scissors', command=lambda: self.player_choice('scissors'))
        self.scissors_button.pack()

        # Label to display the result
        self.result_label = tk.Label(self, text='', font=('Helvetica', 14))
        self.result_label.pack()

    def player_choice(self, player_move):
        # Randomly select the computer's move
        computer_move = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(player_move, computer_move)

        # Update the result label
        self.result_label.config(text=f'Player: {player_move} | Computer: {computer_move}\nResult: {result}')

    def determine_winner(self, player, computer):
        # Determine the winner
        if player == computer:
            return 'Draw!'
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return 'Player wins!'
        else:
            return 'Computer wins!'

# Create and run the game application
if __name__ == '__main__':
    app = RPSGameApp()
    app.mainloop()


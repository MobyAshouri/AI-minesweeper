import tkinter as tk
from random import randint

############################################################################
# Project by Maymunah Hicks & Moby Ashouri
############################################################################
# IMMEDIATE OBSERVATIONS
# ChatGPT generated this code. It implements design patterns like MVC (Model-
# View-Control), Event-Driven-Programming through buttons (without using actual
# events, interestingly), and States. Even more minor design patterns were found.
# I wouldn't even need to modify the code very much if I needed to add a feature.
############################################################################
# ISSUES
# - You cannot place flags
# - The game is resizable, but is not dynamically scaling
# - Buttons remain depressed even after a restart
# - No game difficulty
# - There is no documentation (not the largest issue in the world)
#
# None of these issues can really be solved by implementing a new design
# pattern in my opinion. These issues can all be almost entirely solved 
# through writing more code though. I'd argue that this is a very versatile
# piece of code from a structural perspective.
#
# We could modify the code to be more inline with the Open/Closed Principle
# when including a game difficulty feature, allowing for more modification
# in succeeding projects that utilize this code.
############################################################################


class Minesweeper:
    # This contructor should allow us to determine the size of the grid
    # and the number of bombs so that modifications don't have to be
    # made later on.
    def __init__(self, master, numberOfRows=9, numberOfCols=9, numOfMines=10):
        self.master = master
        self.master.title("Minesweeper")
        self.rows = numberOfRows
        self.cols = numberOfCols
        self.num_mines = numOfMines
        self.flags = self.num_mines
        self.create_widgets()
        self.create_board()
        self.place_mines()

    def create_widgets(self):
        self.flag_label = tk.Label(self.master, text="Flags: " + str(self.flags))
        self.flag_label.grid(row=0, column=0, columnspan=3)
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart)
        self.restart_button.grid(row=0, column=3, columnspan=6)
        self.buttons = [[None]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j] = tk.Button(self.master, width=3, height=1, command=lambda i=i, j=j: self.reveal(i, j))
                self.buttons[i][j].grid(row=i+1, column=j)

    def create_board(self):
        self.board = [[0]*self.cols for _ in range(self.rows)]

    def place_mines(self):
        for _ in range(self.num_mines):
            row, col = randint(0, self.rows-1), randint(0, self.cols-1)
            while self.board[row][col] == -1:
                row, col = randint(0, self.rows-1), randint(0, self.cols-1)
            self.board[row][col] = -1
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and self.board[i][j] != -1:
                        self.board[i][j] += 1

    def reveal(self, row, col):
        if self.board[row][col] == -1:
            self.buttons[row][col].config(text="*", relief=tk.SUNKEN, state=tk.DISABLED)
            self.game_over()
        elif self.board[row][col] == 0:
            self.buttons[row][col].config(relief=tk.SUNKEN, state=tk.DISABLED)
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and self.buttons[i][j]['state'] == tk.NORMAL:
                        self.reveal(i, j)
        else:
            self.buttons[row][col].config(text=str(self.board[row][col]), relief=tk.SUNKEN, state=tk.DISABLED)

    def game_over(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="*", relief=tk.SUNKEN, state=tk.DISABLED)
                else:
                    self.buttons[i][j].config(state=tk.DISABLED)

    def restart(self):
        self.flags = self.num_mines
        self.flag_label.config(text="Flags: " + str(self.flags))
        self.create_board()
        self.place_mines()
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
                self.master.update()    # even using the update() function on our root window doesn't work.
                # The only REAL solution to this sort of issue is to destroy this window and
                # completely redraw it
                
                ############################################################################
                # The state argument is causing the button to remain depressed after a restart.
                #
                # The argument can be set to NORMAL, ACTIVE, or DISABLED. Setting this value
                # to ACTIVE or DISABLED makes the game unplayable as new tiles cannot be revealed.
                #
                # There is no solution to this (other than redrawing the entire program's window)
                # due to the limitaions of Tkinter. I am writing this on a windows computer, and
                # and the bug might not even exist on a different OS.
                #
                # To ensure maximum OS compatibility, we could make a web app instead using
                # JavaScript, HTML, and CSS.
                ############################################################################
                

def main():
    # Our root window is not resizeable, so we will
    # make the window a single size. If this wasn't
    # an assignment, I'd consider making the window
    # rescale dynamically.
    root = tk.Tk()
    root.resizable(False, False)
    game = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()

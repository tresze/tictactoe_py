#tictactoe.py
import os
from random import randint

def printgrid():
    print("\n" + grid[0], "|", grid[1], "|", grid[2])
    print("---------")
    print(grid[3], "|", grid[4], "|", grid[5])
    print("---------")
    print(grid[6], "|", grid[7], "|", grid[8], "\n")

def user_input(t):
    # checking the turn (even = Player 1 (X), odd = Player 2 (O))
    if t % 2 == 0:
        pl = "1"
        mark = "X"
    else:
        pl = "2"
        mark = "O"

    correctinput = False
    while correctinput == False:
        number = input("Player " + pl + "'s turn: ")
        if number not in accepted_chars:
            print("Invalid input! You can write: 1/2/3/4/5/6/7/8/9") # taking a foolproof input from the user

        elif grid[cells[number]] != " ":
            print("This spot is taken! Please choose another one.") # this doesn't let the user overwrite an existing mark

        else:
            correctinput = True

    print()

    # printing the mark into the grid with the help of the "cells" dictionary
    grid[cells[number]] = mark
    os.system("clear")
    printgrid()

# generates a random position for the computer's mark
def computer():
    freecells = []
    for x in range(0, 9):
        if grid[x] == " ":
            freecells.append(x)
    rnd = randint(0, len(freecells) - 1)
    grid[freecells[rnd]] = "X"
    os.system("clear")
    printgrid()

def is_game_ended():
    isGameWon = False

    # winning combos in the grid
    if grid[0] == grid[1] and grid[1] == grid[2] and grid[0] != " ":
        isGameWon = True
    if grid[3] == grid[4] and grid[4] == grid[5] and grid[3] != " ":
        isGameWon = True
    if grid[6] == grid[7] and grid[7] == grid[8] and grid[6] != " ":
        isGameWon = True
    if grid[0] == grid[3] and grid[3] == grid[6] and grid[0] != " ":
        isGameWon = True
    if grid[1] == grid[4] and grid[4] == grid[7] and grid[1] != " ":
        isGameWon = True
    if grid[2] == grid[5] and grid[5] == grid[8] and grid[2] != " ":
        isGameWon = True
    if grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != " ":
        isGameWon = True
    if grid[2] == grid[4] and grid[4] == grid[6] and grid[2] != " ":
        isGameWon = True

    if isGameWon:
        if menu_choice == "2" and turn % 2 == 1:
            print("Computer won!\n")
            return True
        else:
            print("You won!\n")
            return True

    # checking for a tie
    for value in grid:
        if value == " ":
            return False
    print("It's a tie!\n")
    return True

# player vs. player mode
def with_mate():
    turn = 0
    printgrid()
    while is_game_ended() == False:
        user_input(turn)
        turn += 1

# player vs. computer mode
def with_com():
    global menu_choice, turn
    
    turn = 0
    printgrid()
    while is_game_ended() == False:
        if turn % 2 == 0:
            computer()
        else:
            user_input(turn)
        turn += 1

def regame():
    re = "0"
    while re != "y" or re != "n":
        re = input("Do you want to play again (Y/N)? ").upper()
        if re == "Y":
            os.system("clear")
            menu()   
        elif re == "N":
            exit()
        else:
            print("Please write a letter \"y\" or a letter \"n\".\n")

def menu():
    global grid, turn, menu_choice

    while True:
        print("\n************MAIN MENU**************\n")
        print("1: Game with mate\n2: Game with computer\n3: Quit\n")

        menu_choice = input("The number of your choice: ")

        grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        os.system("clear")

        if menu_choice == "1":
            with_mate()
            regame()
        elif menu_choice == "2":
            with_com()
        # elif menu_choice == "3":
        #     print("com_vs_com()")
        elif menu_choice == "3":
            exit() 
        else:
            print("Invalid input! Please enter: 1 / 2 / 3")
            menu() 

grid = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

accepted_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # this is for checking whether the user input is correct

# dictionary for mapping the numpad (input) numbers with the list (grid) numbers
cells = {
            "7": 0,
            "8": 1,
            "9": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "1": 6,
            "2": 7,
            "3": 8
        }

menu()


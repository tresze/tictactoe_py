#tictactoe.py

def printgrid():
    print("\n" + grid[0], "|", grid[1], "|", grid[2])
    print("---------")
    print(grid[3], "|", grid[4], "|", grid[5])
    print("---------")
    print(grid[6], "|", grid[7], "|", grid[8], "\n")

def user_input(t):
    if t % 2 == 0:
        pl = "1"
        mark = "X"
    else:
        pl = "2"
        mark = "O"

    number = input("Player " + pl + ": ")
    while number not in accepted_chars: 
            print("Invalid input! You can write: 1/2/3/4/5/6/7/8/9")
            number = input("Player " + pl + ": ")

    print()

    if number == "7":
        grid[0] = mark
        printgrid()
    elif number == "8":
        grid[1] = mark
        printgrid()
    elif number == "9":
        grid[2] = mark
        printgrid()
    elif number == "4":
        grid[3] = mark
        printgrid()
    elif number == "5":
        grid[4] = mark
        printgrid()
    elif number == "6":
        grid[5] = mark
        printgrid()
    elif number == "1":
        grid[6] = mark
        printgrid()
    elif number == "2":
        grid[7] = mark
        printgrid()
    elif number == "3":
        grid[8] = mark
        printgrid()

def is_game_ended():
    for value in grid:
        if value == " ":
            return False
    return True

def with_mate():
    turn = 0
    printgrid()
    while is_game_ended() == False:
        user_input(turn)
        turn += 1
    print("Game ended.\n")

def menu():
    print("\n************MAIN MENU**************\n")
    print("1: Game with mate\n2: Game with computer\n3: Computer vs computer\n4: Quit\n")
   
    while True:
        menu_choice = input("The number of your choice: ")
        if menu_choice == "1":
            with_mate()
        elif menu_choice == "2":
            print("with_com()")
        elif menu_choice == "3":
            print("com_vs_com()")
        elif menu_choice == "4":
            exit() 
        else:
            print("Invalid input! Please enter: 1 / 2 / 3 / 4")
            menu() 

grid = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

accepted_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

menu()


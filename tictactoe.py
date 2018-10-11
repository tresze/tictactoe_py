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

    correctinput = False
    while correctinput == False:
        number = input("Player " + pl + "'s turn: ")
        if number not in accepted_chars:
            print("Invalid input! You can write: 1/2/3/4/5/6/7/8/9")

        elif grid[cells[number]] != " ":
            print("This spot is taken! Please choose another one.")

        else:
            correctinput = True

    print()

    grid[cells[number]] = mark
    printgrid()

def is_game_ended():
    isGameWon = False

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
        print("You won!\n")
        return True

    for value in grid:
        if value == " ":
            return False
    print("It's a tie!\n")
    return True

def with_mate():
    turn = 0
    printgrid()
    while is_game_ended() == False:
        user_input(turn)
        turn += 1

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


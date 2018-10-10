#tictactoe.py

def printgrid():
    print(grid[0], "|", grid[1], "|", grid[2])
    print("---------")
    print(grid[3], "|", grid[4], "|", grid[5])
    print("---------")
    print(grid[6], "|", grid[7], "|", grid[8])

def user_input_x():
    numberx = input("Player 1: ")
    while numberx not in accepted_chars: 
            print("Invalid input! You can write: 1/2/3/4/5/6/7/8/9")
            numberx = input("Player 1: ")

    print()

    if numberx == "7":
        grid[0] = "X"
        printgrid()
        print()
    elif numberx == "8":
        grid[1] = "X"
        printgrid()
        print()
    elif numberx == "9":
        grid[2] = "X"
        printgrid()
        print()
    elif numberx == "4":
        grid[3] = "X"
        printgrid()
        print()
    elif numberx == "5":
        grid[4] = "X"
        printgrid()
        print()
    elif numberx == "6":
        grid[5] = "X"
        printgrid()
        print()
    elif numberx == "1":
        grid[6] = "X"
        printgrid()
        print()
    elif numberx == "2":
        grid[7] = "X"
        printgrid()
        print()
    elif numberx == "3":
        grid[8] = "X"
        printgrid()
        print()

def user_input_o():
    numbero = input("Player 2: ")
    while numbero not in accepted_chars: 
            print("Invalid input! You can write: 1/2/3/4/5/6/7/8/9")
            numbero = input("Player 2: ")

    print()

    if numbero == "7":
        grid[0] = "O"
        printgrid()
        print()
    elif numbero == "8":
        grid[1] = "O"
        printgrid()
        print()
    elif numbero == "9":
        grid[2] = "O"
        printgrid()
        print()
    elif numbero == "4":
        grid[3] = "O"
        printgrid()
        print()
    elif numbero == "5":
        grid[4] = "O"
        printgrid()
        print()
    elif numbero == "6":
        grid[5] = "O"
        printgrid()
        print()
    elif numbero == "1":
        grid[6] = "O"
        printgrid()
        print()
    elif numbero == "2":
        grid[7] = "O"
        printgrid()
        print()
    elif numbero == "3":
        grid[8] = "O"
        printgrid()
        print()

def with_mate():
    print()
    isgridfull = False
    printgrid()
    print()
    while isgridfull == False:
        user_input_x()
        user_input_o()
        if grid[0] != " " and grid[1] != " " and grid[2] != " " and grid[3] != " " and grid[4] != " " and grid[5] != " " and grid[6] != " " and grid[7] != " " and grid[8] != " ":
            isgridfull = True

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


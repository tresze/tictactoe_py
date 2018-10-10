#tictactoe.py

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

def show():
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])


def menu():
    print("\n************MAIN MENU**************\n")
    print("1: Game with mate\n2: Game with computer\n3: Computer vs computer\n4: Quit\n")
    
    menu_choice = False
    menu_choice = str(input("The number of your choice: "))
   
    while True:
        if menu_choice == "1":
            print("with_mate()")
            menu()
        elif menu_choice == "2":
            print("with_com()")
            menu()
        elif menu_choice == "3":
            print("com_vs_com()")
            menu()
        elif menu_choice == "4":
            exit() 
        else:
            print("Invalid input! Please enter: 1 / 2 / 3 / 4")
            menu() 


print(menu())
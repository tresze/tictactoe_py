board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

table_full = False

def show():
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])


def menu():
    print("\n************MAIN MENU**************")
    print(" ")
    print("1: Game with mate\n2: Game with computer\n3: Computer vs computer\n4: Quit""")
    
#    menu_choice = False
    menu_choice = str(input("The number of your choice: "))
   
    while True:
        if menu_choice == "1":
            with_mate()
        elif menu_choice == "2":
            with_com()
        elif menu_choice == "3":
            com_vs_com()
        elif menu_choice == "4":
            exit() 
        else:
            print("\nInvalid input! Please enter: 1 / 2 / 3 / 4")
            menu() 


def gamerx():
    try:
        cell = int(input("\nGamer X, select a spot: "))
    except ValueError:
        print("\nInvalid input! Please enter a number between 0-9!")
        gamerx()
    if cell >= 0 and cell <= 9:
        if board[cell] != 'x' and board[cell] != 'o':
            board[cell] = 'x'
            show()
        else:
            print('\nThis spot is taken!')
            gamerx()
    else:
        print("\nInvalid input! Please enter a number between 0-9!")
        gamerx()

def gamero():
    try:
        cell = int(input("\nGamer o, select a spot: "))
    except ValueError:
        print("\nInvalid input! Please enter a number between 0-9!")
        gamero()
    if cell >= 0 and cell <= 9:
        if board[cell] != 'x' and board[cell] != 'o':
            board[cell] = 'o'
            show()
        else:
            print('\nThis spot is taken!')
            gamero()
    else:
        print("\nInvalid input! Please enter a number between 0-9!")
        gamero()

def with_mate():
    while table_full == False:
        gamerx()
        gamero() 
        
     
        
        
        
menu()       
        
















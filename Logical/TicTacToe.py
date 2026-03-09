import random
board = [[" "]*3 for _ in range(3)] 
def print_board():
    for row  in board:
        print(row)

def check_win(player):
    # rows checker 
    for i in range(3):
        if board[i][0]== board[i][1] == board[i][2]== player:
            return True

     #column checker       
    for i in range(3):
        if board[0][i]== board[1][i] == board[2][i] ==player:
            return True

     # diagonal checker        
    for i in range(3):
        if board[0][0]== board[1][1] == board[2][2] ==player:
            return True
        if board[0][2]== board[1][1] == board[2][0] ==player:
            return True

    return False

for turn in range(9):
    if turn % 2 == 0 :
        print("Computer Turn's")
        while True:
            row= random.randint(0,2)
            col=random.randint(0, 2)
            if board[row][col]==" ":
                board[row][col]="O"
                break
    else:
        print("user Turn's")
        while True:
            row= random.randint(0, 2)
            col= random.randint(0, 2)
            if board[row][col] == " " :
                board[row][col]="X"
                break
            else:
                print("Cell already filled.")
    print_board()
    
    if turn % 2 == 0:
        if check_win("O"):
            print("Computer Wins")
            break
    else:
        if check_win("X"):
            print("User Wins")
            break

else:
    print("Game Draw")

#Tic Tac Toe Game
#Computer = X
#User = O

from random import randrange
difficulty = 0
hardRobot = 0

#2D list for board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

#Winning Combos
winner = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    
    [0, 4, 8],
    [2, 4, 6]
]


print("""
+=======================+
| Welcome to Tic Tac Toe|
+=======================+
""")


#Difficulty Selection
print("Choose your difficulty:")
print("1. Normal Mode")
print("2. Hard Mode")
selection = input("Enter difficulty mode: ")

difficulty = int(selection) # Converts the input to an integer

match difficulty:
    case 1:
        print("""
+=======================+
|   Difficulty:  Easy   |
+=======================+
""")
    case 2:
        print("""
+=======================+
|   Difficulty:  Hard   |
+=======================+
""")
        hardRobot = 1
    case _:
        print("\nPlease enter a valid difficulty level.")


def x_turn():
    print("""
+=======================+
|         X TURN        |
+=======================+
""")


def o_turn():
    print("""
+=======================+
|         O TURN        |
+=======================+
""")


#Tic Tac Toe Board
def board_open(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + row[0] + "   |   " + row[1] + "   |   " + row[2] + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


#Identify Winning Combos
def gold(board, player):
    pos = [
        board[0][0], board[0][1], board[0][2],
        board[1][0], board[1][1], board[1][2],
        board[2][0], board[2][1], board[2][2]
    ]

    for combo in winner:
        if (pos[combo[0]] == player and
            pos[combo[1]] == player and
            pos[combo[2]] == player):
            return True

    return False


#Identify empty spaces
def free(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                empty.append((i, j))
    return empty


#Computer first move in center(X)
board[1][1] = "X"
o_turn()
board_open(board)


while True:
    #User's move
    while True:
        user_move = input("Enter your move (1-9): ")

        
        #If user enter a move that is 1-9 receive a "Try Again" message
        if user_move not in "123456789":
            print("""
+=======================+
|  ONLY 1-9 TRY AGAIN!  |
+=======================+
""")
            continue
        
        #If user enter a move that is occupied receive a "Try Again" message
        move = int(user_move) - 1
        row = move // 3
        col = move % 3

        if board[row][col] in ["X", "O"]:
            print("""
+=======================+
| CANNOT BE TRY AGAIN!! |
+=======================+
""")
            continue
        #User move = O
        board[row][col] = "O"
        break

    x_turn()
    board_open(board)
    
    #Checks for winning combo, if there is atleast 1 combo print ("You Win")
    if gold(board, "O"):
        print("""
+=======================+
|    YOU WINNNNN!!!!    |
+=======================+
""")
        break

    #Checks if theres no more free space and no winning combo, print ("Its a Tie")
    if len(free(board)) == 0:
        print("""
+=======================+
|    ITS A TIEEE!!!!    |
+=======================+
""")
        break

    #Computer move = "X"
    #Checks for empty spaces to occupy
    #Easy
    empty = free(board)
    index = randrange(len(empty))
    row, col = empty[index]

    board[row][col] = "X"
    if hardRobot == 1:
        #Hard
        hardRobot = 0 # So it only runs once

        empty = free(board)
        index = randrange(len(empty))
        row, col = empty[index]

        board[row][col] = "X"
        
        

    o_turn()
    board_open(board)

    #Checks for winning combo in computer moves, if there is atleast 1 combo print ("You Lose")
    if gold(board, "X"):
        print("""
+=======================+
|    YOU LOSEEEE!!!!    |
+=======================+
""")
        break
    
    #Checks if theres no more free space and no winning combo, print ("Its a Tie")
    if len(free(board)) == 0:
        print("""
+=======================+
|    ITS A TIEEE!!!!    |
+=======================+
""")
        break

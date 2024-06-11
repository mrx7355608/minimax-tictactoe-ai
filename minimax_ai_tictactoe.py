import random

# Setup a tic tac toe board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
human_mark = "X"
ai_mark = "O"

def main():
    gameover = False
    turn = "human"
    winner = None
    while gameover != True:
        display_board()    

        if turn == "human":
            make_move()
            turn = "computer"
        else:
            print("Computer is thinking...")
            computer_random_move()
            turn = "human"
            
        # Check for winner
        winner = check_winner()
        if winner is not None:
            display_board()
            print("\n--------------")
            print("   GAMEOVER   ")
            print("--------------")
            if winner == "tie":
                print("It's a tie")
                gameover = True
                continue
            print(f"{winner} has won the game!")
            gameover = True

# Print the tic tac toe board
def display_board():
    print()
    for i in range(0, 3):
        for j in range(0, 3):
            print(f" {board[i][j]} ", end="")
            if j != 2:
                print("|", end="")
        if i != 2:        
            print("\n---|---|---")

    print()
    print()
    return

# Ask player for a move
def ask_move():
    box_num = int(input("Select a box(1-9): "))
    
    # Get coordinates of the selected box
    row = 0
    col = 0
    
    if box_num > 0 and box_num < 4:
        row = 0
        col = box_num - 1
    elif box_num > 3 and box_num < 7:
        row = 1
        col = box_num - 4
    elif box_num > 6 and box_num < 10:
        row = 2
        col = box_num - 7
    else:
        print("Invalid box number")
        return None, None
    return row, col


# Make move
def make_move():
    row, col = ask_move()
    board[row][col] = "X"


# Check for winner
def check_winner():
    # Horizontal checks
    if board[0][0] != " " and board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
                
    elif board[1][0] != " " and board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
        
    elif board[2][0] != " " and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    
    # Vertical checks    
    elif board[0][0] != " " and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
        
    elif board[0][1] != " " and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]
        
    elif board[0][2] != " " and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    
    # Diagonal checks    
    elif board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
        
    elif board[0][2] != " " and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
        
    elif check_tie():
        return "tie"
    
    else:
        return None

def check_tie():
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == " ":
                return False
    return True
    

# Generate a random move for computer to play
def computer_random_move():
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == " ":
            board[row][col] = "O"
            return
        else:
            continue

scores = {
    'X': -1, # minimizing player
    'O': 1, # maximizing player
    'tie': 0
}

def smart_move():
    best_score = float('-inf')
    best_move = {
        'row': '',
        'col': ''
    }

    for i in range(0,3):
        for k in range(0,3):
            if board[i][k] == " ":
                board[i][k] = ai_mark
                score = minimax(board, False)
                board[i][k] = " "
                if score > best_score:
                    best_score = score
                    best_move = {
                        'row': i,
                        'col': k
                    }

    row = best_move['row']
    col = best_move['col']
    board[row][col] = ai_mark

def minimax(gameBoard, is_maximizing_player):
    # Check if are at terminal state (win / draw / loss)
    winner = check_winner()
    if winner is not None:
        return scores[winner]

    if is_maximizing_player:
        best_score = float('-inf')
        for i in range(0,3):
            for k in range(0,3):
                if gameBoard[i][k] == " ":
                    gameBoard[i][k] = ai_mark
                    score = minimax(gameBoard, False)
                    gameBoard[i][k] = " "
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = float('inf')
        for i in range(0,3):
            for k in range(0,3):
                if gameBoard[i][k] == " ":
                    gameBoard[i][k] = human_mark
                    score = minimax(gameBoard, True)
                    gameBoard[i][k] = " "
                    if score < best_score:
                        best_score = score
        return best_score


main()
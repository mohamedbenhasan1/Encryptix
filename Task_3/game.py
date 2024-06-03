import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move(board):
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move! Try again.")
        player_move(board)

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI played:")
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

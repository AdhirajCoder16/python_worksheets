def print_board(board):
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6:
            print('-' * 5)

def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def tic_tac_toe():
    board = [' ']*9
    current_player = 'X'
    for turn in range(9):
        while True:
            print_board(board)
            choice = input(f"Player {current_player}, choose position (1-9): ")
            if choice.isdigit():
                pos = int(choice) - 1
                if 0 <= pos <= 8 and board[pos] == ' ':
                    board[pos] = current_player
                    break
            print("Invalid input. Try again.")
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
    print_board(board)
    print("Game is a tie.")

if __name__ == "__main__":
    tic_tac_toe()

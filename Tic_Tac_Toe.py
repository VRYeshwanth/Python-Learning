board = ['-','-','-','-','-','-','-','-','-']
current_playing = 'X'
game_running = True
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def user_input(board):
    n = int(input("Enter a number (1-9) : "))
    if (n >= 1 and n <= 9) and board[n-1] == '-':
        board[n-1] = current_playing
    else:
        print("Enter valid choice !!!!!")
        user_input(board)

def change_turn():
    global current_playing
    if current_playing  == 'X':
        current_playing = 'O'
    else:
        current_playing = 'X'

def check_horizontal(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        return True
    if board[3] == board[4] == board[5] and board[3] != '-':
        return True
    if board[6] == board[7] == board[8] and board[6] != '-':
        return True
def check_vertical(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        return True
    if board[1] == board[4] == board[7] and board[1] != '-':
        return True
    if board[2] == board[5] == board[8] and board[2] != '-':
        return True
def check_diagnol(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        return True
    if board[2] == board[4] == board[6] and board[2] != '-':
        return True

def check_tie(board):
    global current_playing
    if '-' not in board:
        val = check_win(board)
        if val == False:
            print_board(board)
            print(f"{current_playing} has won")
            exit(0)
        else:
            print("The game has tied")
            exit(0)

def check_win(board):
    global game_running,current_playing
    if check_horizontal(board) or check_vertical(board) or check_diagnol(board):
        game_running = False
    return game_running

def display_result(board):
    global game_running,current_playing
    if game_running == False:
        print_board(board)
        print(f"{current_playing} has won")

while game_running:
    print_board(board)
    user_input(board)
    check_win(board)
    check_tie(board)
    display_result(board)
    change_turn()
def print_board(board):
    for row in board:
        print('| '.join(row))
        print('---------')


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def main():
    board = [[' ' for i in range(3)] for j in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input('Enter row (0, 1, 2)'))
        col = int(input('Enter col (0, 1, 2)'))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print('Cell is already occupied!')
            continue

        if check_winner(board, player):
            print_board(board)
            print(f'Player {player} wins!')
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print('It\'s a tie!')
            break

        player = 'O' if player == 'X' else 'X'


if __name__ == "__main__":
    main()
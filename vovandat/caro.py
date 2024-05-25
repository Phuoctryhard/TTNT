def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def evaluate(board):
    if is_winner(board, 'x'):
        return 1
    elif is_winner(board, 'o'):
        return -1
    elif is_full(board):
        return 0
    else:
        return None


# def print_game_tree(board, player):
#     print_board(board)
#     result = evaluate(board)
#     if result is not None:
#         if result == 1:
#             print("Người chơi 'x' thắng!")
#         elif result == -1:
#             print("Người chơi 'o' thắng!")
#         else:
#             print("Hòa!")
#         return
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == ' ':
#                 board[i][j] = player
#                 print(f"Lượt của '{player}' - Đánh vào ô ({i + 1}, {j + 1}):")
#                 print_game_tree(board, 'x' if player == 'o' else 'o')


def minimax(board, depth, maximizing_player):
    result = evaluate(board)
    if result is not None:
        return result

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'x'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'o'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'x'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


initial_board = [['o', ' ', ' '],
                 ['x', 'x', 'o'],
                 [' ', 'o', ' ']]

# print_game_tree(initial_board, 'x')

# b) Viết chương trình sử dụng thuật toán Minimax để cho biết “x” nên đánh vào vị trí nào.
best_move = find_best_move(initial_board)
print(f"Người chơi 'x' nên đánh vào ô {best_move}")

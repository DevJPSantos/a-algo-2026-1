"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if action not in actions(board):
        raise Exception("Ação inválida")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    # Verificar linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    if winner(board) is not None:
        return True
    # Se não há vencedor mas ainda há espaços vazios, não é terminal
    if any(EMPTY in row for row in board):
        return False
    return True


def utility(board):
    win = winner(board)
    if win == X: return 1
    if win == O: return -1
    return 0


def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    best_move = None
    for action in actions(board):
        score, _ = min_value(result(board, action))
        if score > v:
            v = score
            best_move = action
    return v, best_move


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    best_move = None
    for action in actions(board):
        score, _ = max_value(result(board, action))
        if score < v:
            v = score
            best_move = action
    return v, best_move
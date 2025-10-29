import numpy as np
from typing import List, Iterable, Tuple
#Representar o tabuleiro de xadrez para o problema das 8 rainhas

Board = List[int]  #Cada índice representa uma coluna, o valor representa a linha da rainha naquela coluna
Move = Tuple[int, int]  #Representa um movimento como (coluna, linha)
N = 8  #Número de rainhas e tamanho do tabuleiro
seed = 42
np.random.seed(seed)

def initialize_board() -> Board:
    """Initialize random board configuration"""
    return np.random.randint(0, N, size=N).tolist()

def conflicts(board: Board) -> int:
    """Calculate the number of conflicts (attacks) between queens on the board"""
    total_conflicts = 0
    for col1 in range(N):
        for col2 in range(col1 + 1, N):
            row1, row2 = board[col1], board[col2]
            if row1 == row2 or abs(row1 - row2) == abs(col1 - col2):
                total_conflicts += 1
    return total_conflicts

def neighbors(board: Board) -> Iterable[Move]:
    """Generate all possible moves for the queens on the board"""
    for col in range(N):
        for row in range(N):
            if board[col] != row:
                yield (col, row)

def apply_move(board: Board, move: Move) -> Board:
    """Apply a move to the board and return the new board configuration"""
    col, row = move
    new_board = board.copy()
    new_board[col] = row
    return new_board

def generate_dict_conflicts(board: Board) -> dict:
    """Generate a dictionary of moves and their resulting conflict counts"""
    dict_conflicts = {}
    for move in neighbors(board):
        new_board = apply_move(board, move)
        dict_conflicts[move] = conflicts(new_board)
    sorted_conflicts = dict(sorted(dict_conflicts.items(), key=lambda item: item[1]))
    return sorted_conflicts
"""
board = [0, 2, 7, 3, 2, 6, 2, 3]  # exemplo qualquer
dict_conflicts = generate_dict_conflicts(board)
list_conflicts = []
for move, conf in dict_conflicts.items():
    list_conflicts.append(move)
    #print(f'Move: {move}, Conflicts: {conf}')

limit_iterations = 10
for i in range(limit_iterations):
    new_move = list_conflicts.pop(0)
    print(new_move)
"""
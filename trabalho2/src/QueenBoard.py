import numpy as np
from typing import List, Iterable, Tuple
import time
#TODO: Corrigir calculo da media de reinícios e movimentos
#TODO: Implementar métrica de tempo

Board = List[int]  #Cada índice representa uma coluna, o valor representa a linha da rainha naquela coluna
Move = Tuple[int, int]  #Representa um movimento como (coluna, linha)
N = 8  #Número de rainhas e tamanho do tabuleiro
#seed = 42
np.random.seed()#seed)

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

def hill_climb_with_lateral(board: Board, limit_break: int) -> Tuple[Board, int, float]:
    current_conflicts = conflicts(board)
    reset_counter = 0
    aux_counter = 0
    total_moves = 0

    while current_conflicts != 0:
        next_move = next_move_with_lateral(board, limit_break)

        if next_move == (8, 8):
            # only reset if board is not solved
            if current_conflicts != 0:
                reset_counter+=1
                if aux_counter>0:
                    total_moves += aux_counter
                aux_counter = 0
                #print (f"{reset_counter}: Generating new board...")
                board = initialize_board()
        else:
            board = apply_move(board, next_move)
            aux_counter+=1
		
        # update conflicts AFTER applying move or reset
        current_conflicts = conflicts(board)
        #print(f"Current conflicts: {current_conflicts}")
		
    if reset_counter > 0:
        move_mean = total_moves / reset_counter
    else:
        move_mean = aux_counter
    return board, reset_counter, move_mean

def hill_climb_with_random(board: Board) -> Tuple[Board, int, float]:
    reset_counter = 0
    aux_counter = 0
    total_moves = 0
    current_conflicts = conflicts(board)
    while current_conflicts !=0:
        restart_test = np.random.randint(0, 20)
        if restart_test == 1:
            reset_counter+=1
            if aux_counter>0:
                total_moves += aux_counter
            aux_counter = 0
            #print(f"{reset_counter}: Generating new board...")
            board = initialize_board()
        possible_conflicts = generate_dict_conflicts(board)
        next_move = next(
            iter(possible_conflicts)
        )
        v = possible_conflicts[next_move]
        if (1 != 0): #TODO: ???????
            board = apply_move(board, next_move)
            aux_counter+=1
            #print(board)
            #print(current_conflicts)
            current_conflicts = v
    if reset_counter > 0:
        move_mean = total_moves / reset_counter
    else:
        move_mean = aux_counter
    return board, reset_counter, move_mean

def next_move_with_lateral(board: Board, limit_break) -> Move:
    possible_conflicts = generate_dict_conflicts(board) # Dicionário ordenado dos movimentos e seus conflitos
    current_conflicts = conflicts(board)
    best_conflict_current_neighbor = best_conflict(possible_conflicts)

    # 1. Encontrar o conjunto de movimentos que minimizam conflitos (ascendentes ou laterais)
    best_moves = []
    min_conf_next_step = float('inf')

    # Percorrer os movimentos ordenados
    for move, conf in possible_conflicts.items():
        if conf < min_conf_next_step:
            min_conf_next_step = conf
            best_moves = [(move, conf)]
        elif conf == min_conf_next_step:
            best_moves.append((move, conf))
        elif conf > min_conf_next_step:
            # Como o dicionário já está ordenado, podemos parar
            break

    # 2. Se houver movimentos ascendentes (melhores que o estado atual)
    if min_conf_next_step < current_conflicts:
        # Pega o primeiro movimento ascendente encontrado (o mais simples)
        move, conf = best_moves[0]
        #print(f"Chosen move: {move} (Ascendente: {current_conflicts} -> {conf})")
        return move

    # 3. Se houver movimentos laterais (plateau)
    if min_conf_next_step == current_conflicts and current_conflicts > 0:
        tested = 0
        
        # Filtra apenas os movimentos que são laterais (já fizemos isso implicitamente em best_moves)
        lateral_moves = [item for item in best_moves if item[1] == current_conflicts]
        
        for move, conf in lateral_moves:
            if tested >= limit_break:
                break
                
            tested += 1
            possible_board = apply_move(board, move)
            next_conflicts = generate_dict_conflicts(possible_board)
            best_conflict_from_move = best_conflict(next_conflicts)
            
            #print(f"Testing lateral move {move}: best(next)={best_conflict_from_move}, best(current)={best_conflict_current_neighbor}")

            # Se a melhor vizinhança do novo estado (lateral) for estritamente melhor 
            # que a melhor vizinhança do estado atual.
            if best_conflict_from_move < best_conflict_current_neighbor:
                #print(f"Chosen move: {move} (Lateral: {current_conflicts} -> {conf} com melhor vizinhança)")
                return move
            
    # 4. Se não houver movimentos ascendentes e nenhum lateral que melhore a melhor vizinhança (pico ou plateau sem saída)
    #print("No better/promising lateral move found — returning sentinel (8, 8)")
    return (8, 8)

def best_conflict(conflicts: dict) -> int:
    """Return the conflict value of the best move from the provided dict.
    Assumes `conflicts` is ordered with best (lowest) first."""
    if not conflicts:
        return float('inf')  # no moves => treat as infinitely bad
    # get the first value in the dict (works on Python 3.7+ where dict preserves insertion order)
    _, conf = next(iter(conflicts.items()))
    return conf


#board = [0, 4, 7, 3, 2, 6, 2, 3] # exemplo qualquer
#board = [7, 4, 0, 3, 1, 6, 2, 2] # exemplo com loop
#board = initialize_board()
#result = hill_climb_with_random(board)
#print("Result Board", result)
limit_break = 10
def main():
    board = initialize_board()

    t_lateral = time.time()
    solution, aux_counter, aux_mean = hill_climb_with_lateral(board, limit_break)
    t_lateral = time.time()- t_lateral

    print(f'One solution lateral moves:\nTime: {t_lateral:.10f}s, Reset counter: {aux_counter}, Move mean: {aux_mean:.2f}\nSolution: {solution}\n')

    t_random = time.time()
    solution, aux_counter, aux_mean = hill_climb_with_random(board)
    t_random = time.time()- t_random

    print(f'One solution random restart:\nTime: {t_random:.10f}s, Reset counter: {aux_counter}, Move mean: {aux_mean:.2f}\nSolution: {solution}\n')
    
    list_solutions_lateral = []
    reset_counter_lateral = 0
    move_mean_lateral = 0
    t_lateral_all = time.time()
    while len(list_solutions_lateral) < 92:
        board = initialize_board()
        solution, aux_counter, aux_mean = hill_climb_with_lateral(board, 10)
        if not solution in list_solutions_lateral:
            list_solutions_lateral.append(solution)
            if(reset_counter_lateral==0):
                reset_counter_lateral = aux_counter
                move_mean_lateral = aux_mean
            else:
                reset_counter_lateral += aux_counter
                move_mean_lateral = np.mean([move_mean_lateral, aux_mean])
            #print(solution)
    t_lateral_all = time.time() - t_lateral_all
    print(f'All solutions lateral moves:\nTime: {t_lateral_all:.10f}s, Reset counter: {reset_counter_lateral}, Success rate: {(92.0/(reset_counter_lateral+1))*100:.2f}%, Move mean: {move_mean_lateral:.2f}\n')
    
    list_solutions_random = []
    reset_counter_random = 0
    move_mean_random = 0
    t_random_all = time.time()
    while len(list_solutions_random) < 92:
        board = initialize_board()
        solution, aux_counter, aux_mean = hill_climb_with_random(board)
        if not solution in list_solutions_random:
            if(reset_counter_random==0):
                reset_counter_random = aux_counter
                move_mean_random = aux_mean
            else:
                reset_counter_random += aux_counter
                move_mean_random = np.mean([move_mean_random, aux_mean])
            list_solutions_random.append(solution)
    t_random_all = time.time() - t_random_all
    print(f'All solutions random restart:\nTime: {t_random_all:.10f}s, Reset counter: {reset_counter_random}, Success rate: {(92.0/(reset_counter_random+1))*100:.2f}%, Move mean: {move_mean_random:.2f}\n')

if __name__=='__main__':
    main()


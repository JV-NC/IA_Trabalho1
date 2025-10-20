#TODO: colocar as funções dos algoritmos de busca aqui
import Adj
from Adj import Pos
from typing import Dict, List, Optional, Tuple

def bfs(adj: Dict[Pos, List[Pos]],start: Pos, goal: Pos)-> Optional[List[Pos]]:
    """Execute Breadth-First Search to find path from start to goal, if it exists"""
    queue = [start]

    tracker: Dict[Pos,Optional[Pos]] = {start:None} #indicates where each node came from

    while queue:
        current = queue.pop(0) #remove from start (FIFO)

        if current == goal: #path found
            break

        for neighbor in adj.get(current,[]):
            if neighbor not in tracker:
                queue.append(neighbor)
                tracker[neighbor] = current
    
    if goal not in tracker: #path not found
        return None
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    path.reverse()
    return path

def dfs(adj: Dict[Pos, List[Pos]],start: Pos, goal: Pos)-> Optional[List[Pos]]:
    """Execute Depth-First Search to find path from start to goal, if it exists"""
    queue = [start]

    tracker: Dict[Pos,Optional[Pos]] = {start:None} #indicates where each node came from

    while queue:
        current = queue.pop() #remove from top (FILO)

        if current == goal: #path found
            break

        for neighbor in adj.get(current,[]):
            if neighbor not in tracker:
                queue.append(neighbor)
                tracker[neighbor] = current
    
    if goal not in tracker: #path not found
        return None
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    path.reverse()
    return path
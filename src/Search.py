import Adj
from Adj import Pos
from typing import Dict, List, Optional, Tuple, Union, Set
from Heuristics import manhattan_distance, euclidian_distance
from memory_profiler import profile

@profile
def bfs(adj: Dict[Pos, List[Pos]], start: Pos, goal: Pos)-> Tuple[Optional[List[Pos]], int, int]:
    """Execute Breadth-First Search to find path from start to goal, if it exists"""
    generated = 0
    expanded = 0
    queue = [start]

    tracker: Dict[Pos,Optional[Pos]] = {start:None} #indicates where each node came from

    while queue:
        current = queue.pop(0) #remove from start (FIFO)
        expanded += 1

        if current == goal: #path found
            break

        for neighbor in adj.get(current,[]):
            if neighbor not in tracker:
                queue.append(neighbor)
                tracker[neighbor] = current
                generated += 1
    
    if goal not in tracker: #path not found
        return None
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    path.reverse()
    return path, expanded, generated

@profile
def dfs(adj: Dict[Pos, List[Pos]], start: Pos, goal: Pos)-> Tuple[Optional[List[Pos]], int, int]:
    """Execute Depth-First Search to find path from start to goal, if it exists"""
    queue = [start]
    generated = 0
    expanded = 0

    tracker: Dict[Pos,Optional[Pos]] = {start:None} #indicates where each node came from

    while queue:
        current = queue.pop() #remove from top (FILO)
        expanded += 1

        if current == goal: #path found
            break

        for neighbor in adj.get(current,[]):
            if neighbor not in tracker:
                queue.append(neighbor)
                tracker[neighbor] = current
                generated += 1
    
    if goal not in tracker: #path not found
        return None
    
    path = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    path.reverse()
    return path, expanded, generated

@profile
def greedy_search(adj: Dict[Pos, List[Pos]], heuristic: Dict[Pos, Union[int, float]], start: Pos, goal: Pos)-> Tuple[Optional[List[Pos]], int, int]:
    """Execute Greedy Best-First Search to find path from start to goal, if it exists"""

    frontier: List[Pos] = [start]
    tracker: Dict[Pos, Optional[Pos]] = {start:None}
    generated = 0
    expanded = 0

    visited: set[Pos] = set()

    while frontier:
        current = min(frontier,key=lambda pos: heuristic.get(pos, float('inf')))
        frontier.remove(current)
        expanded += 1

        if current == goal: #path found
            break

        visited.add(current)

        for neighbor in adj.get(current, []):
            if neighbor not in visited and neighbor not in frontier:
                tracker[neighbor] = current
                frontier.append(neighbor)
                generated += 1

    if goal not in tracker: #path not found
        return None

    path: List[Pos] = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    
    path.reverse()
    return path, generated, expanded

@profile
def a_star_search(adj: Dict[Pos, List[Pos]], heuristic: Dict[Pos, Union[int, float]], start: Pos, goal: Pos)-> Tuple[Optional[List[Pos]], int, int]:
    """Execute A* Search to find path from start to goal, if it exists"""

    frontier: List[Pos] = [start]
    tracker: Dict[Pos, Optional[Pos]] = {start:None}
    current_cost: Dict[Pos, Union[int, float]] = {start: 0}
    generated = 0
    expanded = 0

    while frontier:
        current = min(frontier,key=lambda pos: current_cost[pos] + heuristic.get(pos, float('inf')))
        frontier.remove(current)
        expanded += 1

        if current == goal: #path found
            break

        for neighbor in adj.get(current, []):
            new_cost = current_cost[current]+1
            if neighbor not in current_cost or new_cost < current_cost[neighbor]:
                tracker[neighbor] = current
                current_cost[neighbor] = new_cost
                if neighbor not in frontier:
                    frontier.append(neighbor)
                    generated += 1

    if goal not in tracker: #path not found
        return None

    path: List[Pos] = []
    current = goal
    while current:
        path.append(current)
        current = tracker[current]
    
    path.reverse()
    return path, generated, expanded
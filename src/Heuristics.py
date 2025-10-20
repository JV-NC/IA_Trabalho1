import Adj
from Adj import Pos
from typing import Dict, List, Optional, Tuple
import math

def manhattan_distance(adj: Dict[Pos, List[Pos]], goal: Pos)-> Dict[Pos, int]:
    """Get manhattan distance for every node to goal, returns a Dict of all nodes and their distance to the goal"""
    heuristic: Dict[Pos, int] = {}
    for k in adj.keys():
        heuristic[k] = abs(k[0] - goal[0]) + abs(k[1] - goal[1])

    return heuristic

def euclidian_distance(adj: Dict[Pos, List[Pos]], goal: Pos)-> Dict[Pos, int]:
    """Get euclidian distance for every node to goal, returns a Dict of all nodes and their distance to the goal"""
    heuristic: Dict[Pos, int] = {}
    for k in adj.keys():
        heuristic[k] = math.sqrt((k[0]-goal[0])**2 + (k[1]-goal[1])**2)

    return heuristic
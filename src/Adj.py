from typing import Tuple,List,Dict,Optional

Pos = Tuple[int, int]

file = 'data/maze.txt'

def read_maze(file: str)->List[List[str]]:
    """This function reads maze.txt and returns a matrix"""
    with open(file, 'r') as f:
        maze = [list(linha.strip()) for linha in f]
    return maze

def build_adjacency_list(maze: List[List[str]]) -> Dict[Pos, List[Pos]]:
    """Build the adjacency list using a matrix, removing walls '#' and returns the adjacency list as a Dict"""
    rows = len(maze)
    cols = len(maze[0])

    adj: Dict[Pos, List[Pos]] = {}

    # North, South, East, West
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def valid_position(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#'
    
    # Wander maze
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != '#':  # No walls
                now: Pos = (i, j)
                neighbors: List[Pos] = []
                # Verifiy adjacent neighbors (north, south, east, lest)
                for dl, dc in directions:
                    nl, nc = i + dl, j + dc
                    if valid_position(nl, nc):
                        neighbors.append((nl, nc))
                    adj[now] = neighbors
    
    return adj

def find_positions(maze: List[List[str]]) -> Tuple[Optional[Pos], Optional[Pos]]:
    """Find start (S) and Goal positions"""
    start: Optional[Pos] = None
    goal: Optional[Pos] = None

    for i, row in enumerate(maze):
        for j, pos in enumerate(row):
            if pos == 'S':
                start = (i, j)
            elif pos == 'G':
                goal = (i, j)

    return start, goal

def generate_maze_adj(file: str) -> Tuple[Dict[Pos, List[Pos]], Optional[Pos], Optional[Pos]]:
    """read maze.txt, build adjacency list, find start and goal positions and returns adj list, start and goal"""
    maze = read_maze(file)
    adj = build_adjacency_list(maze)
    start, goal = find_positions(maze)
    return adj, start, goal
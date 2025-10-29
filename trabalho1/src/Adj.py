from typing import Tuple,List,Dict,Optional

Pos = Tuple[int, int]

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

def generate_maze_matrix(adj: Dict[Pos, List[Pos]], rows: int, cols: int, start: Optional[Pos] = None, goal: Optional[Pos] = None)->List[List[str]]:
    """Generate maze matrix using adjacency list, returns maze matrix"""
    maze = [['#' for _ in range(cols)] for _ in range(rows)]

    for pos in adj:
        r, c = pos
        maze[r][c] = '.'

    if start:
        sr, sc = start
        maze[sr][sc] = 'S'

    if goal:
        gr, gc = goal
        maze[gr][gc] = 'G'

    return maze

def mark_path_on_maze(maze: List[List[str]], path: List[Pos]) -> List[List[str]]:
    """Mark path using '*' on maze matrix and return new maze matrix."""
    for r, c in path:
        if maze[r][c] == '.':
            maze[r][c] = '*'
    return maze
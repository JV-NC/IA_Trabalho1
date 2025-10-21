import time
import Adj
from Adj import Pos
import Search
from Heuristics import manhattan_distance, euclidian_distance
from colorama import Fore, Back, Style, init

#TODO: verificar seed, print e criar função separada para plotar profile

def pretty_print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == '#': # Color for walls
                print(Fore.WHITE + cell, end=" ")
            elif cell == '*': # Color for paths
                print(Fore.GREEN + cell, end=" ")
            elif cell == 'S': # Color for the start
                print(Fore.CYAN + cell, end=" ")
            elif cell == 'G': # Color for the goal
                print(Fore.YELLOW + cell, end=" ")
            else: #Color for empty spaces
                print(Fore.LIGHTBLACK_EX + cell, end=" ")
            print(Style.RESET_ALL, end="")
        print()

def main():
    file = 'data/maze.txt'
    algs = ['bfs','dfs','greedy','a_star']
    times={}
    adj, start, goal = Adj.generate_maze_adj(file)

    for alg in algs:
        print(f'Running {alg}...')
        times[alg] = time.time()
        match alg:
            case 'bfs':
                 path, generated, expanded = Search.bfs(adj,start,goal)
            case 'dfs':
                 path, generated, expanded = Search.dfs(adj,start,goal)
            case 'greedy':
                 path, generated, expanded = Search.greedy_search(adj,manhattan_distance(adj,goal),start,goal)
            case 'a_star':
                 path, generated, expanded = Search.a_star_search(adj,manhattan_distance(adj,goal),start,goal)
        times[alg] = time.time() - times[alg]
        if path:
             maze = Adj.mark_path_on_maze(Adj.read_maze(file),path)
             pretty_print_maze(maze)
        print(f'{alg} finished in {times[alg]:.6f} seconds.\n')
        print(f'Generated: {generated}, Expanded: {expanded}\n')

if __name__=='__main__':
    main()
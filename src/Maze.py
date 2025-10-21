import time
import Adj
from Adj import Pos
import Search
from Heuristics import manhattan_distance, euclidian_distance
from typing import List, Dict
from colorama import Fore, Back, Style, init
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import os

os.makedirs('output',exist_ok=True)

#TODO: comentar o codigo

def run_with_memory_profile(alg_function, *args):
    """Run a search algorithm and returns its memory usage"""
    mem_usage = memory_usage((alg_function,args))
    return mem_usage

def plot_memory(mem_usage, alg):
    """plot memory usage of a algorithm and save it on output/"""
    plt.figure()
    plt.plot(mem_usage)
    plt.title(f'Memory Usage - {alg.upper()}')
    plt.xlabel('Time (samples)')
    plt.ylabel('Memory (MiB)')
    plt.grid(True)
    plt.savefig(f'output/{alg}_memory_plot.png')
    plt.close()

def pretty_print_maze(maze: List[List[str]]):
    """Print the maze matrix with diferent colors"""
    for row in maze:
        for item in row:
            if item == '#': # Color for walls
                print(Fore.WHITE + item, end=" ")
            elif item == '*': # Color for paths
                print(Fore.GREEN + item, end=" ")
            elif item == 'S': # Color for the start
                print(Fore.CYAN + item, end=" ")
            elif item == 'G': # Color for the goal
                print(Fore.YELLOW + item, end=" ")
            else: #Color for empty spaces
                print(Fore.LIGHTBLACK_EX + item, end=" ")
            print(Style.RESET_ALL, end="")
        print()

def path_file(maze: List[List[str]], alg: str, time: float, generated: int = None, expanded: int = None):
    """Save the algorithm path on a .txt file with its time and quantity of nodes generated and expanded"""
    with open(f'output/path_{alg}.txt','w') as out:
        if maze:
            for row in maze:
                out.write(''.join(row)+'\n')
        out.write(f'Time: {time:.10f}s, Generated: {generated}, Expanded: {expanded}\n')

def main():
    file = 'data/maze.txt' #maze.txt
    algs = ['bfs','dfs','greedy_manhattan','a_star_manhattan','greedy_euclidian','a_star_euclidian'] #types of algorithms used
    times: Dict[str, float] = {}
    adj, start, goal = Adj.generate_maze_adj(file)

    for alg in algs:
        print(f'Running {alg}...')
        times[alg] = time.time() #start time
        match alg:
            case 'bfs':
                path, generated, expanded = Search.bfs(adj,start,goal)
            case 'dfs':
                path, generated, expanded = Search.dfs(adj,start,goal)
            case 'greedy_manhattan':
                path, generated, expanded = Search.greedy_search(adj,manhattan_distance(adj,goal),start,goal)
            case 'a_star_manhattan':
                path, generated, expanded = Search.a_star_search(adj,manhattan_distance(adj,goal),start,goal)
            case 'greedy_euclidian':
                path, generated, expanded = Search.greedy_search(adj,euclidian_distance(adj,goal),start,goal)
            case 'a_star_euclidian':
                path, generated, expanded = Search.a_star_search(adj,euclidian_distance(adj,goal),start,goal)
        times[alg] = time.time() - times[alg] #end time

        def algorithm_function():
            """reads the current alg and return its function with parameters"""
            match alg:
                case 'bfs':
                    return Search.bfs(adj, start, goal)
                case 'dfs':
                    return Search.dfs(adj, start, goal)
                case 'greedy_manhattan':
                    return Search.greedy_search(adj, manhattan_distance(adj, goal), start, goal)
                case 'a_star_manhattan':
                    return Search.a_star_search(adj, manhattan_distance(adj, goal), start, goal)
                case 'greedy_euclidian':
                    return Search.greedy_search(adj, euclidian_distance(adj, goal), start, goal)
                case 'a_star_euclidian':
                    return Search.a_star_search(adj, euclidian_distance(adj, goal), start, goal)
        
        mem_usage = run_with_memory_profile(algorithm_function)
        plot_memory(mem_usage, alg)

        if path: #path found
             maze = Adj.mark_path_on_maze(Adj.read_maze(file),path)
             path_file(maze,alg,times[alg],generated,expanded)
             pretty_print_maze(maze)
        else: #path not found
            path_file([],alg,times[alg],generated,expanded)
            print('Path could not be found.')
        
        print(f'{alg} finished in {times[alg]:.10f} seconds.\n')
        print(f'Generated: {generated}, Expanded: {expanded}\n')

if __name__=='__main__':
    main()
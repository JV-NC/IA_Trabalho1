import time
import Adj
from Adj import Pos
import Search
from Heuristics import manhattan_distance, euclidian_distance

#TODO: usar time para tempo, sys ou memory_profiler para memoria, e contadores para nos gerados e expandidos

def main():
    file = 'data/maze.txt'
    
    adj, start, goal = Adj.generate_maze_adj(file)

    print('BFS:')
    time_bfs = time.time()
    Search.bfs(adj,start,goal)
    time_bfs -=time.time()
    time_bfs = abs(time_bfs)

    print('DFS:')
    time_dfs = time.time()
    Search.dfs(adj,start,goal)
    time_dfs -=time.time()
    time_dfs = abs(time_dfs)

    print('Greedy Best-first Search:')
    time_greedy = time.time()
    Search.greedy_search(adj,manhattan_distance(adj,goal),start,goal)
    time_greedy -=time.time()
    time_greedy = abs(time_greedy)

    print('A*:')
    time_a_star = time.time()
    Search.a_star_search(adj,manhattan_distance(adj,goal),start,goal)
    time_a_star -=time.time()
    time_a_star = abs(time_a_star)

    print(f'BFS time: {time_bfs}')
    print(f'DFS time: {time_dfs}')
    print(f'Greedy time: {time_greedy}')
    print(f'A* time: {time_a_star}')

if __name__=='__main__':
    main()
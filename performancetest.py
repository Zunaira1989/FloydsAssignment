import Floyds
import sys
import time


if __name__ == '__main__':
    
    graph = [[0, 7, Floyds.NO_PATH, 8],
             [Floyds.NO_PATH, 0, 5, Floyds.NO_PATH],
             [Floyds.NO_PATH, Floyds.NO_PATH, 0,   2],
             [Floyds.NO_PATH, Floyds.NO_PATH, Floyds.NO_PATH, 0]
             ]
    
    # create a working copy of the graph to pass to the function.
    dist = [] 
    for i in graph:
        new_i=[]
        for j in i:
            new_i.append(j)
        dist.append(new_i)
    
    # run each test 500 times in order to test performace differences
    
    #recursive_test
    started_at = time.time()
    for _ in range(75000):
        Floyds.floydWarshall(dist,0)
    
    recursive_time = time.time() - started_at
    
    print('It took the recursive function {}s to complete 75000 runs'.format(round(recursive_time,2)))
    
    dist = [] 
    for i in graph:
        new_i=[]
        for j in i:
            new_i.append(j)
        dist.append(new_i)
    
    #iterative_test
    started_at = time.time()
    for _ in range(75000):
        Floyds.floydWarshallIterative(dist)
    
    iterative_time = time.time() - started_at
    
    print('It took the iterative function {}s to complete 75000 runs'.format(round(iterative_time,2)))
    
    dist = [] 
    for i in graph:
        new_i=[]
        for j in i:
            new_i.append(j)
        dist.append(new_i)
import sys


MAX_LENGTH = 4
NO_PATH = sys.maxsize
 
 #The recursive fucntion takes in a 'dist' parameter which is the matrix that the distance values will be updated into, it also takes in a second parameter which is the number of intermediate verticies
def floydWarshall(dist, numberOfIntermmediateVerticies):
    
    #If the number of intermediate verticies reaches the maximum length of the original input graph, then we need to just return the distance values as they will have all been calculated
    if numberOfIntermmediateVerticies >= MAX_LENGTH:
        return dist 
 
    # This loop calculates the shortest distance from vertex i to vertex j considering the number of intermediate verticies
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            dist[i][j] = min(dist[i][j],
                             dist[i][numberOfIntermmediateVerticies] + dist[numberOfIntermmediateVerticies][j])
 
    # This is where the recursion happens, the number of intermediate verticies is increased by 1
    return floydWarshall(dist, numberOfIntermmediateVerticies+1)


# This is the iterative version of the function. 
def floydWarshallIterative(dist):
    for k in range(MAX_LENGTH):
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
import sys
import Floyds


if __name__ == "__main__":
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
    
    dist = list(dist)
    
    dist = Floyds.floydWarshall(dist, 0) 
    
    for i in range(Floyds.MAX_LENGTH):
        for j in range(Floyds.MAX_LENGTH):
            if(dist[i][j] == Floyds.NO_PATH): # If the distance is sys.maxsize, rather than print the large number, prints NO_PATH instead
                print("%7s" % ("NO_PATH"), end=" ") # Format the printed line to 7 characters wide using a space at the end of the line
            else:
                print("%7d" % (dist[i][j]), end=' ') # Format the printed line to 7 characters wide using a space at the end of the line
            if j == Floyds.MAX_LENGTH-1:
                print() # print a new line character.
    
    dist = [] 
    for i in graph:
        new_i=[]
        for j in i:
            new_i.append(j)
        dist.append(new_i)
                
    dist = Floyds.floydWarshallIterative(dist)
    
    for i in range(Floyds.MAX_LENGTH):
        for j in range(Floyds.MAX_LENGTH):
            if(dist[i][j] == Floyds.NO_PATH): # If the distance is sys.maxsize, rather than print the large number, prints NO_PATH instead
                print("%7s" % ("NO_PATH"), end=" ") # Format the printed line to 7 characters wide using a space at the end of the line
            else:
                print("%7d" % (dist[i][j]), end=' ') # Format the printed line to 7 characters wide using a space at the end of the line
            if j == Floyds.MAX_LENGTH-1:
                print() # print a new line character.
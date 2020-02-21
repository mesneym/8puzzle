import numpy as np
from collections import deque
from Nodes import Node




#############################################
# @brief - prints the state of a puzzle
#
# @param - puzzle state as a matrix
#
# @return - None
#############################################
def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

############################################
# @brief- This function generates the path
#         from the root Node to goal Node 
#
# @param- 1.dictionary holding explored nodes
#          2. goal node 
#
# @return None
############################################
def generatePath(dictionary,node):
    cur = node
    l = []
    count = 0
    while(cur.parentIndex != -1):
        l.append(cur.nodeState)
        count += 1
        cur = dictionary[cur.parentIndex]

    l.append(cur.nodeState) 
    f = open('./nodePath.txt','w')
    for i in range(len(l)-1,-1,-1):
        n = l[i].flatten('F')
        np.savetxt(f,n.reshape(1,len(n)),delimiter=' ',fmt='%d')
    f.close()


#############################################
# @brief- This function converts node array
#         (node State) to a string. Used by 
#         set in storing unique elements
#
# @param- node 
#
# @return String representation of node state
#############################################
def convertArrayToString(node):
    H = node.nodeState
    s = ""
    for i in range(3):
        for j in range(3):
            s += str(int(H[i,j]))
    return s

#############################################
# @brief- This function converts node array
#         (node State) to a string. Used by 
#         set in storing unique Nodes
#
# @param- node 
#
# @return String representation of node state
#############################################
def solvability(node):
    h = root.nodeState.flatten() 
    invCount = 0
    for i in range(0,8):
        for j in range(i+1,9):
            if(h[i] and h[i]>h[j]):
                invCount += 1
    return (invCount%2 == 0)


#############################################
# @brief- This function converts node array
#         (node State) to a string. Used by 
#         set in storing unique elements
#
# @param- 1.newNode - new Node to be added
#         2.nodesQueue - Queue storing nodes
#         3.visitedNodes- Explored nodes
#
# @return String representation of node state
#############################################
def addNode(nodesQueue,newNode,visitedNodes):
    s = convertArrayToString(newNode)
    if(s not in visitedNodes):
        nodesQueue.appendleft(newNode)
        return True
    return False


# Reading goal and initial matrix from file
gx,gy,gz,x,y,z= np.loadtxt('mat.csv', delimiter=',' ,unpack=True, skiprows=1)
mat = np.column_stack((x,y,z))
mat= mat.astype(int)
goalMat= np.column_stack((gx,gy,gz))
goalMat= goalMat.astype(int)

#Initializing root node with matrix and setting 
# appropriate indices
root = Node(mat,0,-1)
nodesQueue = deque()
nodesQueue.appendleft(root)

#Parameters
#nodesExplored- dictionary to store visitednodes. Helps index
#               in generating path from goal node to root
# visitednodes- Necessary as we don't wan't to explore a given node
#               State twice
direction =np.array([[0,1],[1,0],[-1,0],[0,-1]])
nodesExplored = {}
visitedNodes = set()


count = 1 #counts number of nodes seen so far

if( not solvability(root)): #To be modified
    print("not solvable")

else:
    f = open('./NodesInfo.txt','w')
    fd = open('./Nodes.txt','w')

    while(len(nodesQueue) != 0):
        node = nodesQueue.pop()

        #mark node as visited by updating nodesExplored and visitedNodes
        nodesExplored[node.index] = node  
        visitedNodes.add(convertArrayToString(node)) 
        
        f.write(str(node.index)+ " " + str(node.parentIndex) + " "+str(0) + "\n")
        n = node.nodeState.flatten('F')
        np.savetxt(fd,n.reshape(1,len(n)),delimiter=' ',fmt='%d')

        if((node.nodeState == goalMat).all()): # check if goal is reached
            generatePath(nodesExplored,node) # generate path from goal node  
            break;                           # from goal node to root node
        
        #moveTile in 4 directions(up,left,down,right) and 
        #add new nodes to nodeQueue
        for i in range(4): 
            status,newNode =node.moveTile(direction[i,:])
            if(status):
                newNode.index = count
                newNode.parentIndex = node.index

                if(addNode(nodesQueue,newNode,visitedNodes)):
                    count += 1
    f.close()
    fd.close()


    fname = 'nodePath.txt'
    data = np.loadtxt(fname)
    if len(data[1]) is not 9:
        print("Format of the text file is incorrect, retry ")
    else:
        for i in range(0, len(data)):
            if i == 0:
                print("Start Node")
            elif i == len(data)-1:
                print("Achieved Goal Node")
            else:
                print("Step ",i)
            print_matrix(data[i])
            print()
            print()


import numpy as np
from collections import deque
from Nodes import Node


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
    while(cur.parentIndex != -1):
        print(cur.nodeState)
        print("=============")
        cur = dictionary[cur.parentIndex]
    print(cur.nodeState)


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
    return True


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
    print("Not solvable")
else:

    # f = open('./NodesInfo.txt','w')
    # f.write(str(root.index)+ " " + str(root.parentIndex)+"\n")
     
    # fd = open('./Nodes.txt','w')
    # np.savetxt(fd,root.nodeState.flatten())

    while(len(nodesQueue) != 0):
        node = nodesQueue.pop()

        if((node.nodeState == goalMat).all()): # check if goal is reached
            generatePath(nodesExplored,node) # generate path from goal node  
            break;                           # from goal node to root node
        
        #mark node as visited by updating nodesExplored and visitedNodes
        nodesExplored[node.index] = node  
        visitedNodes.add(convertArrayToString(node)) 

        #moveTile in 4 directions(up,left,down,right) and 
        #add new nodes to nodeQueue
        for i in range(4): 
            status,newNode =node.moveTile(direction[i,:])
            if(status):
                newNode.index = count
                newNode.parentIndex = node.index

                if(addNode(nodesQueue,newNode,visitedNodes)):
                    # f.write(str(newNode.index)+ " " + str(newNode.parentIndex) + "\n")
                    # fd.write("\n")
                    # n= newNode.nodeState.flatten().reshape(9,1))
                    # np.savetxt(fd,n)
                    count += 1
    # f.close()
    # fd.close()


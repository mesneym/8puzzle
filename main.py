import numpy as np
from collections import deque
from Nodes import Node

def generatePath(dictionary,node):
    cur = node
    while(cur.parentIndex != -1):
        print(cur.nodeState)
        print("=============")
        cur = dictionary[cur.parentIndex]
    print(cur.nodeState)


def convertArrayToString(node):
    H = node.nodeState
    s = ""
    for i in range(3):
        for j in range(3):
            s += str(int(H[i,j]))
    return s

def addNode(nodesQueue,newNode,visitedNodes):
    s = convertArrayToString(newNode)
    if(s not in visitedNodes):
        nodesQueue.appendleft(newNode)
        return True
    return False

gx,gy,gz,x,y,z= np.loadtxt('mat.csv', delimiter=',' ,unpack=True, skiprows=1)
mat = np.column_stack((x,y,z))
goalMat= np.column_stack((gx,gy,gz))

root = Node(mat,0,-1)
nodesQueue = deque()
nodesQueue.appendleft(root)

direction =np.array([[0,1],[1,0],[-1,0],[0,-1]])
nodesExplored = {}
visitedNodes = set()

count = 1
while(True):
    node = nodesQueue.pop()

    if((node.nodeState == goalMat).all()):
        generatePath(nodesExplored,node)
        break;
   
    nodesExplored[node.index] = node
    visitedNodes.add(convertArrayToString(node))
    for i in range(4):
        status,newNode =node.moveTile(direction[i,:])
        if(status):
            newNode.index = count
            newNode.parentIndex = node.index
            if(addNode(nodesQueue,newNode,visitedNodes)):
                count += 1
           



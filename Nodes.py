import numpy as np
import copy

class Node:
    def __init__(self,state,index,parentIndex):
        self._nodeState = None
        self._index = -1
        self._parentIndex = -1
        self._blankTileLoc = -1

    @index.setter
    def index(self,val):
        self._index = val

    @parentIndex.setter
    def parentIndex(self,val):
        self._parentIndex = val

    @property 
    def blankTileLocation(self):
        if(blankTileLoc != -1):
            return blankTileLoc
        else:
            for i in range(3):
                for j in range(3):
                    if(self._nodeState[i,j]==0):
                        self._blankTileLoc = [i,j]
                        return self._blankTileLoc

    @property 
    def nodeState(self):
        return self._nodeState 

    def actionMoveLeft(self):
        i,j= np.add(self._blankTileLoc,[-1,0])
        if(i>=0  and i<3 and j>=0 and j<3):
            newNode = copy.deepcopy(self)
            temp = newNode._nodeState[i,j]
            newNode.nodeState[i,j]=newNode.nodeState[newNode.blackTileLoc[0,0],newNode._blackTileLoc[0,1]]
            newNode._nodeState[newNode._blackTileLoc[0,0],newNode._blackTileLoc[0,1]] = temp
            return [True,newNode]
        return [False,newNode]

    def actionMoveRight(self):
        i,j= np.add(self._blankTileLoc,[1,0])
        if(i>=0  and i<3 and j>=0 and j<3):
            newNode = copy.deepcopy(self)
            temp = newNode._nodeState[i,j]
            newNode.nodeState[i,j]=newNode.nodeState[newNode.blackTileLoc[0,0],newNode._blackTileLoc[0,1]]
            newNode._nodeState[newNode._blackTileLoc[0,0],newNode._blackTileLoc[0,1]] = temp
            return [True,newNode]
        return [False,NewNode]


    def actionMoveUp(self):
        i,j= np.add(self._blankTileLoc,[0,1])
        if(i>=0  and i<3 and j>=0 and j<3):
            newNode = copy.deepcopy(self)
            temp = newNode._nodeState[i,j]
            newNode.nodeState[i,j]=newNode.nodeState[newNode.blackTileLoc[0,0],newNode._blackTileLoc[0,1]]
            newNode._nodeState[newNode._blackTileLoc[0,0],newNode._blackTileLoc[0,1]] = temp
            return [True,newNode]
        return [False,newNode]

    def actionMoveDown(self):
        if(i>=0  and i<3 and j>=0 and j<3):
            newNode = copy.deepcopy(self)
            temp = newNode._nodeState[i,j]
            newNode.nodeState[i,j]=newNode.nodeState[newNode.blackTileLoc[0,0],newNode._blackTileLoc[0,1]]
            newNode._nodeState[newNode._blackTileLoc[0,0],newNode._blackTileLoc[0,1]] = temp
            return [True,newNode]
        return [False,newNode]



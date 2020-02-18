import numpy as np
class Node:
    def __init__(self,state,index,parentIndex):
        self._nodeState = None
        self._index = -1
        self._parentIndex = -1
        self._blankTileLoc = -1


    def blankTileLocation(self):
        if(blankTileLoc != -1):
            return blankTileLoc
        else:
            for i in range(3):
                for j in range(3):
                    if(self._nodeState[i,j]==0):
                        self._blankTileLoc = [i,j]
                        return self._blankTileLoc

    def actionMoveLeft(self):
        i,j= np.add(self._blankTileLoc,[-1,0])
        if(i>=0  and i<3 and j>=0 and j<3):
            temp = self._nodeState[i,j]
            self._nodeState[i,j]=self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]]
            self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]] = temp


    def actionMoveRight(self):
        i,j= np.add(self._blankTileLoc,[1,0])
        if(i>=0  and i<3 and j>=0 and j<3):
            temp = self._nodeState[i,j]
            self._nodeState[i,j]=self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]]
            self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]] = temp

    def actionMoveUp(self):
        i,j= np.add(self._blankTileLoc,[0,1])
        if(i>=0  and i<3 and j>=0 and j<3):
            temp = self._nodeState[i,j]
            self._nodeState[i,j]=self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]]
            self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]] = temp

    def actionMoveDown(self):
        i,j= np.add(self._blankTileLoc,[0,-1])
        if(i>=0  and i<3 and j>=0 and j<3):
            temp = self._nodeState[i,j]
            self._nodeState[i,j]=self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]]
            self._nodeState[self._blackTileLoc[0,0],self._blackTileLoc[0,1]] = temp



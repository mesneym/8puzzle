###############################################
# @file - This file contains the implementation
#        of Node class
###############################################
import numpy as np
import copy


class Node(object):

    ################################################
    # @brief - constructor for node class 
    # @param - 1.state-State of matrix puzzle
    #          2.index- Index of node 
    #          3.parentIndex- Index of parent node
    ################################################
    def __init__(self,state,index,parentIndex):
        self._nodeState = state 
        self._index = index
        self._parentIndex = parentIndex
        self._blankTileLoc = -1 #stores location of blankTile

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self,val):
        self._index = val

    @property
    def parentIndex(self):
        return self._parentIndex 

    @parentIndex.setter
    def parentIndex(self,val):
        self._parentIndex = val

    @property
    def nodeState(self):
        return self._nodeState

    @property 
    def blankTileLocation(self):
        if(self._blankTileLoc != -1):
            return self._blankTileLoc
        else:
            for i in range(3):
                for j in range(3):
                    if(self._nodeState[i,j]==0):
                        self._blankTileLoc = [i,j]
                        return self._blankTileLoc

    @blankTileLocation.setter
    def blankTileLocation(self,newloc):
        self._blankTileLoc = newloc

    @property 
    def nodeState(self):
        return self._nodeState 

    def moveTile(self,direction):
        i,j= np.add(self.blankTileLocation,direction)
        if(i>=0  and i<3 and j>=0 and j<3):
            newNode = copy.deepcopy(self)
            temp = newNode.nodeState[i,j]
            newNode.nodeState[i,j]= 0
            newNode.nodeState[newNode.blankTileLocation[0], \
                              newNode.blankTileLocation[1]] = temp
            newNode.blankTileLocation = [i,j]
            return [True,newNode]
        return [False,None]





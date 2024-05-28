#import random

class node:
    def __init__(self,data):
        self.x = 0
        self.y = 0
        self.parent = data
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

def operation(cnode,rule):
    x = cnode.x
    y = cnode.y

    if rule == 1:
        if x < j1:
            x = j1
        else:
            return None
    elif rule == 2:
        if y < j2:
            y = j2
        else:
            return None
    elif rule == 3:
        if x > 0:
            x = 0
        else:
            return None
    elif rule == 4:
        if y > 0:
            y = 0
        else:
            return None
    elif rule == 5:
        if x + y >= j1:
            y = y - (j1 - x)
            x = j1
        else:
            return None
    elif rule == 6:
        if x + y >= j2:
            x = x - (j2 - y)
            y = j2
        else:
            return None
    elif rule == 7:
        if x + y < j1:
            x = x + y
            y = 0
        else:
            return None
    elif rule == 8:
        if x + y < j2:
            y = x + y
            x = 0
        else:
            return None
    if x == cnode.x and y == cnode.y:
        return None
    nextnode = node(cnode)
    nextnode.x = x
    nextnode.y = y
    nextnode.parent = cnode
    return nextnode

def isGoalNode(cnode,gnode):
    if cnode.x == gnode.x:
        return True
    return False

def printPath(cnode):
    temp = cnode
    list1 = []
    while(temp != None):
        list1.append(temp)
        temp = temp.parent
    list1.reverse()
    for i in list1:
        print(str(i))    


class Dfsalgo:
    def __init__(self):
        self.dfsStack = []
    def pushNode(self,m):
        self.dfsStack.append(m)
    def pushList(self,l1):
        for m in l1:
            self.dfsStack.append(m)
    def isEmpty(self,l):
        return len(l) == 0
    def popNode(self):
        if self.isEmpty(self.dfsStack):
            return None
        else:
            return self.dfsStack.pop()
    def IsNodeInList(self,node,l):
        for m in l:
            if node.x == m.x and node.y == m.y:
                return True
        return False
    '''def generateRandomSucessor(self,cnode,visitednodeList):
        list1 = []
        listrule = []
        while len(listrule) < 8:
            ruleno = random.randint(1,8)
            if (not ruleno in listrule):
                listrule.append(ruleno)
                nextnode = operation(cnode,ruleno)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    list1.append(nextnode)
        return list1'''
    def generateSequentialSucessor(self,cnode,visitednodeList):
        list1 = []
        for rule in range (1,9):
            nextnode = operation(cnode,rule)
            if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                list1.append(nextnode)
        list1.reverse()
        return list1
    def generateAllSucessors(self,cnode,visitednodeList):
        #list1 = self.generateRandomSucessor(cnode,visitednodeList)
        list1 = self.generateSequentialSucessor(cnode,visitednodeList)
        return list1
    
    def dfsMain(self,initialNode,GoalNode):
        VisitedNodeList = []
        self.dfsStack.append(initialNode)
        while not self.isEmpty(self.dfsStack):
            VisitedNode = self.popNode()
            VisitedNodeList.append(VisitedNode)
            if isGoalNode(VisitedNode,GoalNode):
                return VisitedNode
            sucessornode = self.generateAllSucessors(VisitedNode,VisitedNodeList)
            self.pushList(sucessornode)
        return None
            
if __name__=="__main__":

    j1 = int(input("Enter the capacity of 1st jug: "))
    j2 = int(input("Enter the capacity of 2nd jug: "))
    initialNode = node(None)
    initialNode.x = 0
    initialNode.y = 0
    initialNode.parent = None
    goalNode = node(None)
    goalNode.x = int(input("Enter the amount of water required in 1st Jug: "))
    goalNode.y = 0
    goalNode.parent = None

    solutionNode = Dfsalgo().dfsMain(initialNode,goalNode)

    if solutionNode != None:
        printPath(solutionNode)
    else:
        print("solution not found!")
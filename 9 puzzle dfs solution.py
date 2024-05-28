import math
class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
def operation(cnode,rule):
    x = cnode.x
    y = cnode.y

    if rule == 1:
        x = 0
        y = 1
    elif rule == 2:
        x = 1
        y = 0
    elif rule == 3:
        x = 0
        y = 0
    elif rule == 4:
        x = 1
        y = 1
    elif rule == 5:
        x = 0
        y = 2
    elif rule == 6:
        x = 0
        y = 1
    elif rule == 7:
        x = 1
        y = 2
    elif rule == 8:
        x = 0
        y = 0
    elif rule == 9:
        x = 1
        y = 1
    elif rule == 10:
        x = 2
        y = 0
    elif rule == 11:
        x = 0
        y = 1
    elif rule == 12:
        x = 1
        y = 0
    elif rule == 13:
        x = 2
        y = 1
    elif rule == 14:
        x = 1
        y = 2
    elif rule == 15:
        x = 0
        y = 2
    elif rule == 16:
        x = 1
        y = 1
    elif rule == 17:
        x = 2
        y = 2
    elif rule == 18:
        x = 1
        y = 0
    elif rule == 19:
        x = 2
        y = 1
    elif rule == 20:
        x = 2
        y = 0
    elif rule == 21:
        x = 1
        y = 1
    elif rule == 22:
        x = 2
        y = 2
    elif rule == 23:
        x = 2
        y = 1
    elif rule == 24:
        x = 1
        y = 2
    
    nextnode = node(cnode)
    nextnode.x = x
    nextnode.y = y
    nextnode.parent = cnode
    return nextnode
    
def isGoalNode(cstate,gstate):
    if gstate == cstate:
        return True

def calsum(gstate,cstate):
    sum = 0
    for i in range(3):
        for j in range(3):
            if cstate[i][j] == gstate[i][j]:
                sum += 1

class Dfsalgo:
    def __init__(self):
        self.Stack = []

    def pushNode(self, m):
        self.Stack.append(m)

    def pushList(self, l1):
        for m in l1:
            self.Stack.append(m)

    def isEmpty(self, l):
        return len(l) == 0

    def popNode(self):
        if self.isEmpty(self.Stack):
            return None
        else:
            return self.Stack.pop()

    def IsNodeInList(self, node, l):
        for m in l:
            if node.x == m.x and node.y == m.y:
                return True
        return False
    
    def generateAllSucessors(self, cnode, l, visitednodeList):
        list1 = []
        if cnode.x == 0 and cnode.y == 0:
            for rule in range(1, 3):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 0 and cnode.y == 1:
            for rule in range(3, 6):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 0 and cnode.y == 2:
            for rule in range(6, 8):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 1 and cnode.y == 0:
            for rule in range(8, 11):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 1 and cnode.y == 1:
            for rule in range(11, 15):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 1 and cnode.y == 2:
            for rule in range(15, 18):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 2 and cnode.y == 0:
            for rule in range(18, 20):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 2 and cnode.y == 1:
            for rule in range(20, 23):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        elif cnode.x == 2 and cnode.y == 2:
            for rule in range(23, 25):
                nextnode = operation(cnode, rule)
                if nextnode != None and not self.IsNodeInList(nextnode, visitednodeList):
                    if not(visitednodeList[0].x == nextnode.x and visitednodeList[0].y == nextnode.y):
                        list1.append(nextnode)
        return list1 , cnode

    def dfsMain(self, initialNode, l, goalstate):
        VisitedNodeList = []
        pre = node(None)
        pre.x = 10
        pre.y = 10
        pre.parent = None
        prevnodelist = [pre]
        self.Stack.append(initialNode)
        while not self.isEmpty(self.Stack):
            VisitedNode = self.popNode()
            VisitedNodeList.append(VisitedNode)
            if isGoalNode(l, goalstate):
                return VisitedNode
            sucessornode, prevnode = self.generateAllSucessors(VisitedNode, l, prevnodelist)
            if len(prevnodelist) != 0:
                prevnodelist.pop()
            prevnodelist.append(prevnode)
            #print(prevnodelist)

            # make huristic funtion here to rank the elements with values, then sort and push in stack

            self.pushList(sucessornode)

            #print(self.Stack)

        return None


if __name__ == "__main__":

    l = [[2,8,3],
         [1,6,4],
         [7,0,5]]
    goalstate = [[1,2,3],
                 [8,0,4],
                 [7,6,5]]

    initialNode = node(None)
    initialNode.x = 2
    initialNode.y = 1
    initialNode.parent = None
    
    solutionNode = Dfsalgo().dfsMain(initialNode, l, goalstate)

    if solutionNode != None:
        print(goalstate)
    else:
        print("solution not found!")
        
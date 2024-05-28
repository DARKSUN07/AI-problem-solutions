class node:
    def __init__(self,data):
        node.x = 0
        node.y = 0
        node.z = 0
        node.parent = data
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

def operation(lnode,rnode,rule):

    x = lnode.x
    y = lnode.y
    z = lnode.z

    a = rnode.x
    b = rnode.y

    #print(lnode)
        
    if z == 0:
        if rule == 1:
            if (x - y == 2 and x >= 2) or (x == 2) or (x == y and x == 2):
                x-=2
                a+=2
            else:
                return None,None
        elif rule == 2:
            if (a == 3 and y>=2) or (a == 0 and y >=2):
                y-=2
                b+=2
            else:
                return None,None
        elif rule == 3:
            if  x > 0 and y > 0 and x == y:
                x-=1
                y-=1
                a+=1
                b+=1
            else:
                return None,None 
        elif rule == 4:
            if x - y == 1 and x > 0:
                x-=1
                a+=1
            else:
                return None,None
        elif rule == 5:
            if (x == 3 and y > 0) or (y + 1 <= a and y > 0):
                y-=1
                b+=1
            else:
                return None,None
        
        nextlnode = node(lnode)
        nextlnode.x = x
        nextlnode.y = y
        nextlnode.z = 1
        nextlnode.parent = lnode

        nextrnode = node(rnode)
        nextrnode.x = a
        nextrnode.y = b
        nextrnode.z = 1
        nextrnode.parent = rnode
        return nextlnode,nextrnode
        
    elif z == 1:

        #print(x,y,a,b)
        
        if rule == 1:
            if (a - b == 2 and a >= 2) or (a == 2):
                a-=2
                x+=2
            else:
                return None,None
        elif rule == 2:
            if (x == 3 and b >= 2) or (x == 0 and b >= 2):
                b-=2
                y+=2
            else:
                return None,None
        elif rule == 3:
            if  a > 0 and b > 0 and a == b:
                a-=1
                b-=1
                x+=1
                y+=1
            else:
                return None,None 
        elif rule == 4:
            if a - b == 1 and a - b == 0 and a > 0:
                a-=1
                x+=1
            else:
                return None,None
        elif rule == 5:
            if (a == 3 and b > 0) or (b + 1 <= x and b > 0) or (a == 0) :
                b-=1
                y+=1
            else:
                return None,None
        nextlnode = node(lnode)
        nextlnode.x = x
        nextlnode.y = y
        nextlnode.z = 0
        nextlnode.parent = lnode

        nextrnode = node(rnode)
        nextrnode.x = a
        nextrnode.y = b
        nextrnode.z = 0
        nextrnode.parent = rnode
        return nextlnode,nextrnode

def isGoalnode(rnode,goalnode):
    if rnode.x == goalnode.x and rnode.y == goalnode.y and rnode.z == goalnode.z:
        return True
    return False

def printpath(lnode,rnode):
    templ = lnode
    tempr = rnode
    l = []
    r = []
    while (templ != None and tempr != None):
        l.append(templ)
        r.append(tempr)
        templ = templ.parent
        tempr = tempr.parent
    l.reverse()
    r.reverse()
    
    for i in range(len(l)):
        print("(",l[i].x,",",l[i].y,")","\t","(",r[i].x,",",r[i].y,")")

class BFSalgo:
    def __init__(self):
        self.queue_l = []
        self.queue_r = []
    def isEmpty(self,queue):
        return len(queue) == 0
    def enqueue(self,l,r):
        self.queue_l.append(l)
        self.queue_r.append(r)
    def dequeue(self):
        self.queue_l.reverse()
        self.queue_r.reverse()
        #print(self.queue_l,self.queue_r)
        return self.queue_l.pop(),self.queue_r.pop()
    def appendList(self,l,r):
        for m in l:
            self.queue_l.append(m)
        for n in r:
            self.queue_r.append(n)
    def isNodeInList(self,node,l):
        for m in l:
            if node.x == m.x and node.y == m.y:
                return True
        return False
    
    def generatingsucessorlist(self,lnode,rnode):
        l = []
        r = []
        for rule in range(1,6):
            #print(rule)
            sucessornode_l,sucessornode_r = operation(lnode,rnode,rule)
            #print(sucessornode_l,sucessornode_r,"This is sucessor node")
            if sucessornode_l != None and sucessornode_r != None:
                l.append(sucessornode_l)
                r.append(sucessornode_r)
            #print(l,r)
        return l,r

    def bfsmain(self,lnode,rnode,goalNode):

        #print(lnode,rnode)
        self.enqueue(lnode,rnode)
        #print(self.queue_l,self.queue_r)

        while not (self.isEmpty(self.queue_l) and self.isEmpty(self.queue_r)):

            visited_l,visited_r = self.dequeue()
            self.queue_l.reverse()
            self.queue_r.reverse()
            #print(self.queue_l,self.queue_r)
            #print(visited_l,visited_r)
            sucessorlist_l,sucessorlist_r= self.generatingsucessorlist(visited_l,visited_r)
            #print(sucessorlist_l,sucessorlist_r)
            if not self.isEmpty(sucessorlist_l):
                self.appendList(sucessorlist_l,sucessorlist_r)
            for i in range(len(sucessorlist_r)):
                if isGoalnode(sucessorlist_r[i],goalNode):
                    return sucessorlist_l[i],sucessorlist_r[i]
            #print("This is queue",self.queue_l,self.queue_r)
        return None,None

if __name__ == "__main__":
    
    initialnode_L = node(None)
    initialnode_L.x = 3
    initialnode_L.y = 3
    initialnode_L.z = 0
    initialnode_L.parent = None

    initialnode_R = node(None)
    initialnode_R.x = 0
    initialnode_R.y = 0
    initialnode_R.z = 0
    initialnode_R.parent = None

    goalnode = node(None)
    goalnode.x = 3
    goalnode.y = 3
    goalnode.z = 1
    goalnode.parent = None

    #print(initialnode_L,initialnode_R,goalnode)
    
    finalnode_l,finalnode_r = BFSalgo().bfsmain(initialnode_L,initialnode_R,goalnode)
    if finalnode_l != None and finalnode_r != None:
        printpath(finalnode_l,finalnode_r)
    else:
        print("Solution not found!")
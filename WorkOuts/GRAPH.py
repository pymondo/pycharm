from collections import  defaultdict


# learn Khan's sorting as well
''' Application . Build systems, task scheduling , pre requise problems'''
''' Topoligical sorting  for DAG - DIRECTED ACYCLIC GRAPH'''
class Graph:
    __doc__ = 'graph is default dict which will have lists'
    def __init__(self,verteces):
        self.graph = defaultdict(list)
        self.v = verteces

    # its just appedning t list if its a child
    def addEdge(self,u, v):
        self.graph[u].append(v)

    # this is for recusrsion.. 1st step is make it visted = true then explore its kid call recusrsivey
    # after all the kids explored add the parent to stack thats all
    def topologicalSortUtil(self, v, visited, stack):
        visited[v]= True

        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v)



    def topologicalSort(self):
        # mark all vertices not visited . its a list [f,f,f,f,f]
        visited = [False]*self.v
        stack = []

        for i in range(self.v):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        print(stack)

    def isCyclic_util(self, recur_stack, visited, v):
        visited[v] = True
        recur_stack[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclic_util(recur_stack, visited, i) == True:
                    return True
            elif recur_stack[i] == True:  # if its visted check weather its already in the current stack.
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recur_stack[v] = False

        return False

    def isCyclic(self):
        # keep track of visting
        rec_stack = [False] * self.v

        # depth first search keep track of depth, while coming out wil make it false. Makes sense think abt it.
        visited = [False] * self.v

        for i in range(self.v):
            if visited[i] == False:
                if self.isCyclic_util(rec_stack, visited, i) == True:
                    return True
        return False

g = Graph(6)
g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(2, 3);
g.addEdge(3, 1);
g.addEdge(4, 2);
g.addEdge(4, 5);
g.addEdge(5, 3);

for i , v in g.graph.items():
    print(i,v)


g.topologicalSort()

#================================================

''' you should find the sorting finish timings and starting time think about it'''
"""The following implementation assumes that the activities
are already sorted according to their finish time"""

def max_activity_selecting_greedy_problem(s,f):
    print(0)
    i = 0

    for j in range(1,len(s)):
        if s[j]>= f[i]:
            i=j
            print(i)

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
max_activity_selecting_greedy_problem(s , f)

'''Prime's Alogorith for minimum spamming tree'''
import  sys

class graph:
    def __init__(self,ver):
        self.v=ver
        self.graph = [[0 for column in range(ver)]
                      for row  in range(ver)]

    def getMin(self,key,mstSet):
        min = sys.maxsize
        minIndex = 0
        for i in range(self.v):
            if key[i]<min and mstSet[i] ==False:
                min= key[i]
                minIndex=i

        return minIndex


    def print_mst(self):
        key = [sys.maxsize]*self.v
        parent = [None]*self.v
        mstSet=[False]*self.v

        key[0] = 0
        parent[0]=-1

        for _ in range(self.v):
            minIndex = self.getMin(key,mstSet)

            mstSet[minIndex] = True

            #update the adjacent vertices
            for v in range(self.v):
                if self.graph[minIndex][v] > 0 and mstSet[v] ==False and self.graph[minIndex][v] < key[v]:
                    key[v] = self.graph[minIndex][v]
                    parent[v] = minIndex

        self.printMST(parent)

    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])



g  = graph(5)
g.graph= [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g.print_mst()


import dimacs
from operator import itemgetter
from queue import Queue

class node:
    def __init__(self,data):
        self.data = data
        self.parent = self
        self.rank = 0


def findSet(x):
    if x is not x.parent:
        x.parent = findSet(x.parent)
    return x.parent

def union(x,y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def przewodnikTurystycznyFindUnion(V,L):
    L.sort( key = itemgetter(2), reverse= True)

    for (x,y,c) in L:                       
        print( "krawedz miedzy", x, "i", y,"o wadze", c )



    sets = [node(i) for i in range(V+1)]
    


    for edge in L:
        union(sets[edge[0]],sets[edge[1]])
        if findSet(sets[1]) is findSet(sets[2]):
            return edge[2]


def testFindUnion():

    V,L,expected = dimacs.loadWeightedGraph("g1")

    print(przewodnikTurystycznyFindUnion(V,L) == expected)

def toAdjList(V,L):
    print (L)

    adj = [[] for _ in range(V+1)]

    for edge in L:
        adj[edge[0]].append((edge[1],edge[2]))
        adj[edge[1]].append((edge[0],edge[2]))

    print (adj)
    return adj



def testBFS():
    V,L,expected = dimacs.loadWeightedGraph("g1")
    adj = toAdjList(V,L)

 
def bfs(adj,s=1,t=2):
    n = len(adj)
    q = Queue()
    visited = [False for _ in range(n)]

    parent = [None for _ in range(n)]
    distance = [None for _ in range(n)]

    q.put(s)
    visited[s] = True

    while q.empty() is False:
        u = q.get()

        for v in adj(u):
            visited[v] = True



testDFS()






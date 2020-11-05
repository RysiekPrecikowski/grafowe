import dimacs
import math

class Node:
    def __init__(self):
        self.edges = {}    # słownik  mapujący wierzchołki do których są krawędzie na ich wagi

    def addEdge( self, to, weight):
        self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                         # o zadanej wadze; a jeśli taka krawędź
                                                          # istnieje, to dodaj do niej wagę

    def delEdge( self, to ):                          # usuń krawędź do zadanego wierzchołka
        del self.edges[to]


    def __repr__(self) -> str:
        return str(self.edges)

class Graph:
    def __init__(self, V, L) -> None:
        self.v = V+1
        self.adj = [ Node() for _ in range(V+1)]
        self.info = [ None for _ in range( V+1 )]

        for (x,y,c) in L:
            self.adj[x].addEdge(y,c)
            self.adj[y].addEdge(x,c)
    

    def mergeVertices(self, x, y):
        #delete from y
        #add to x
        # print("from",y,"to",x)
        # self.print()
        for toV, weight in list(self.adj[y].edges.items()):
            #TODO dodawanie pamietania o usuwanych polaczeniach 
            #TODO dodac info o scalonych wierzcholkach 
            #self.info powinno sie tym zajmowac?

            

            self.adj[y].delEdge(toV)        
            # print(x,y,toV)
            if toV == x:
                # print("ten sam",x,y,toV)
                self.adj[x].delEdge(y)
            else:
                self.adj[x].addEdge(toV,weight)
                self.adj[toV].addEdge(x,weight)
                self.adj[toV].delEdge(y)
            
            # self.print()


    def print(self):
        print()
        for v in self.adj:
            print(self.adj.index(v), v)


from queue import PriorityQueue

def minimumCutPhase(g):
    a = 1
    u = 1

    q = PriorityQueue()

    visited = [False for _ in range(g.v)]
    visited[a] = True
    q.put((0,a))

    
    last = a #ostatni wierzcholek dodany do S
    prev = None #przedostatni wierzcholek dodany do S

    while q.empty() is False:
        prev = u
        weight, u = q.get()

        last = u            # dla porzadku
        
        # print(u,weight)
        # print(u)
        for v, w in g.adj[u].edges.items():
            if visited[v] is False:
                visited[v] = True
                q.put((weight + w, v))


    currentRes = 0

    for v, w in g.adj[last].edges.items():
        currentRes += w
    # print(prev, last, currentRes)
    print(prev, last)
    g.mergeVertices(prev,last)

    # g.print()
    return currentRes



def StoerWagnerAlgorithm(g):
    k = 0
    
    x = g.v

    best = math.inf
    while x >= 2:
        res = minimumCutPhase(g)
        x = 0

        for i in range(g.v):
            if(len(g.adj[i].edges) > 0):
                x+=1

        if best > res:
            best = res

        # print("aktualny",res, "best", best, "zostalo", x)
        
    # print("result:",min(res))
    return best



def testStoerWagner(path):
    V, L, solution = dimacs.loadWeightedGraph(path)
    
    g = Graph(V,L)
    res = StoerWagnerAlgorithm(g)
    print("compare", res, solution)
    return res == solution 


V, L, res = dimacs.loadWeightedGraph("tests/grid5x5")

# for (x,y,c) in L:                        # przeglądaj krawędzie z listy
#   print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj

import time
g = Graph(V,L)

g.print()
start = time.time()


print("powinno byc", res, "a jest", StoerWagnerAlgorithm(g))

print("time:", time.time() - start)

from runAllTests import run
run(testStoerWagner,"/failed/")
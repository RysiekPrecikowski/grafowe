"""
Dany jest graf skierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wieżchołki s i t. Należy znaleźć maksymalny przepływ w grafie G pomiędzy s i t, tzn. funkcję f: E -> N spełniającą warunki definicji przepływu, zapewniającą największą przepustowość.

Do rozwiązania zadania należy wykorzystać algorytm Forda-Fulkersona, porównując dwie strategie znajdowania ścieżek powiększających:

przy użyciu przeszukiwania metodą DFS
przy użyciu przeszukiwania metodą BFS (algorytm Edmondsa-Karpa)
"""

import dimacs 
import queue
from math import inf
from pprint import pp, pprint


class Edge:
    def __init__(self, v, u, cap, flow=0) -> None:
        self.cap = cap #capacity
        self.flow = flow 
        self.v = v
        self.u = u

    def getRes(self):
        return self.cap - self.flow

    def __repr__(self) -> str:
        return "<" + str(self.cap) + "/" + str(self.flow) + ">"
        

class graph:
    def __init__(self, n, edges) -> None:
        self.n = n

        self.start = 1
        self.end = n

        self.matrix = [[None for _ in range(n+1)] for _ in range(n+1)]

        for edge in edges:
            if self.matrix[edge[0]][edge[1]] is None:
                self.matrix[edge[0]][edge[1]] = Edge(edge[0], edge[1], edge[2])
                self.matrix[edge[1]][edge[0]] = Edge(edge[1], edge[0], 0)
            else:
                #TODO chyba ze tylko dodac?
                # self.matrix[edge[0]][edge[1]].cap -= edge[2]
                self.matrix[edge[1]][edge[0]].cap += edge[2]

    

    def FordFulkerson(self):
        def findPath():
            def getFlow():
                v = self.end
                flow = inf

                while v is not self.start:
                    # print("v:", v)
                    # print(self.matrix[parent[v]][v].getRes())
                    flow = min(flow, self.matrix[parent[v]][v].getRes())
                    v = parent[v]
                
                return flow


            q = queue.Queue()

            visited = [False for _ in range(self.n + 1)]
            parent = [None for _ in range(self.n + 1)]

            q.put(self.start)
            visited[self.start] = True
            
            while q.empty() is False:
                u = q.get()
                # print(q.qsize())
  
                if u is self.end:      
                    return parent, getFlow()
                
                for v in range(self.n + 1):
                    if visited[v] is False and self.matrix[u][v] is not None and self.matrix[u][v].getRes() > 0:

                        visited[v] = True
                        parent[v] = u
                        q.put(v)
                
            return None, 0
        
        def updateRes(flow, path):
            v = self.end
            while v is not self.start:
                self.matrix[path[v]][v].flow += flow
                self.matrix[v][path[v]].flow -= flow

                v = path[v]
        

        res = 0
        # print("path", findPath())
        

        path, flow = findPath()

        while path is not None :
            # print()
            # print()
            # print("path", findPath())
            # print()

            # pprint(self.matrix)
            # print(res)
            res += flow
            updateRes(flow, path)
            path, flow = findPath()


        
        print(res)

        return res



def testFulkerson(path):
    n, edges, solution = dimacs.loadDirectedWeightedGraph(path)
    
    g = graph(n,edges)

    return g.FordFulkerson() == solution 



n, edges, solution = dimacs.loadDirectedWeightedGraph("tests/flow/grid100x100")
# print(n, edges)

g = graph(n,edges)
# pprint(g.matrix)

# res = g.FordFulkerson()

# print(solution is res)

import runAllTests

runAllTests.run(testFulkerson, directory = "/tests/flow/")
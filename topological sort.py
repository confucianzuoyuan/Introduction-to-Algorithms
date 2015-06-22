class Graph:
    def __init__(self):
        self.V = []

class Vertex:
    def __init__(self, x):
        self.key = x
        self.color = 'white'
        self.d = 10000
        self.f = 10000
        self.pi = None
        self.adj = []
        self.next = None

class Solution:
    def Dfs(self, G):
        for u in G.V:
            u.color = 'white'
            u.pi = None
        global time
        time = 0
        for u in G.V:
            if u.color == 'white':
                self.DfsVisit(G, u)

    def DfsVisit(self, G, u):
        global time
        time = time + 1
        u.d = time
        u.color = 'gray'
        for v in u.adj:
            if v.color == 'white':
                self.DfsVisit(G, v)
                v.pi = u
        u.color = 'black'
        time = time + 1
        u.f = time

    def TopologicalSort(self, G):
        LinkedList = Vertex('#')
        self.Dfs(G)
        G.V.sort(key=lambda v:v.f)
        for v in G.V:
            v.next = LinkedList.next
            LinkedList.next = v
        return LinkedList

if __name__ == '__main__':
    undershorts = Vertex('undershorts') 
    socks = Vertex('socks') 
    pants = Vertex('pants') 
    shoes = Vertex('shoes') 
    belt = Vertex('belt')
    shirt = Vertex('shirt') 
    tie = Vertex('tie')
    jacket = Vertex('jacket') 
    watch = Vertex('watch')

    undershorts.adj = [pants, shoes]
    socks.adj = [shoes]
    pants.adj = [belt, shoes]
    shoes.adj = []
    belt.adj = [jacket]
    shirt.adj = [belt, tie]
    tie.adj = [jacket]
    jacket.adj = []
    watch.adj = []

    G = Graph()
    G.V = [undershorts,socks,pants,shoes,belt,shirt,tie,jacket,watch]

    m = Solution()
    Sort_List = m.TopologicalSort(G)
    p = Sort_List
    while p.next != None:
        print p.next.key, p.next.f
        p = p.next
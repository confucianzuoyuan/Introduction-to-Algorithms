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
                v.pi = u
                self.DfsVisit(G, v)
        u.color = 'black'
        time = time + 1
        u.f = time

if __name__ == '__main__':
    u,v,w,x,y,z = [Vertex(i) for i in ['u','v','w','x','y','z']]

    u.adj = [v, x]
    v.adj = [y]
    w.adj = [y, z]
    x.adj = [v]
    y.adj = [x]
    z.adj = [z]

    G = Graph()
    G.V = [u,v,w,x,y,z]

    m = Solution()
    m.Dfs(G)

    for v in G.V:
        print v.key, v.color, v.d, v.f
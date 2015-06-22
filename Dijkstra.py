class Graph:
    def __init__(self):
        self.V = []
        self.w = {}

class Vertex:
    def __init__(self, x):
        self.key = x
        self.color = 'white'
        self.d = 10000
        self.pi = None
        self.adj = []

class Solution():
    def InitializeSingleSource(self, G, s):
        for v in G.V:
            v.d = 10000
            v.pi = None
        s.d = 0

    def Relax(self, u, v, w):
        if v.d > u.d + w[(u, v)]:
            v.d = u.d + w[(u, v)]
            v.pi = u

    def Dijkstra(self, G, w, s):
        self.InitializeSingleSource(G, s)
        S = set()
        Q = G.V[:]
        while Q != []:
            u = self.ExtractMin(Q, S)
            S.add(u)
            for v in u.adj:
                self.Relax(u, v, w)

    def ExtractMin(self, Q, S):
        Q.sort(key=lambda v: v.d)
        return Q.pop(0)



if __name__ == '__main__':
    s = Vertex('s')
    t = Vertex('t')
    y = Vertex('y')
    x = Vertex('x')
    z = Vertex('z')

    s.adj = [t, y]
    y.adj = [t, z, x]
    t.adj = [x, y]
    x.adj = [z]
    z.adj = [x, s]

    G = Graph()
    G.V = [s, t, y, x, z]
    G.w = {
        (s,t):10,
        (s,y):5,
        (t,y):2,
        (y,t):3,
        (t,x):1,
        (y,z):2,
        (x,z):4,
        (z,x):6,
        (y,x):9,
        (z,s):7
    }

    m = Solution()
    m.Dijkstra(G, G.w, s)


    for v in G.V:
        if v != s:
            print v.key, v.d, v.pi.key
        else:
            print v.key, v.d, v.pi
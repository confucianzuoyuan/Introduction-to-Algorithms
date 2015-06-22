class Graph:
    def __init__(self):
        self.V = []

class Vertex:
    def __init__(self, x):
        self.key = x
        self.color = 'white'
        self.d = 10000
        self.pi = None
        self.adj = []

class Solution:
    def BFS(self, G, s):
        for u in G.V:
            if u != s:
                u.color = 'white'
                u.d = 10000
                u.pi = None
        s.color = 'gray'
        s.d = 0
        s.pi = None
        Q = []
        Q.append(s)
        while Q != []:
            u = Q.pop(0)
            for v in u.adj:
                if v.color == 'white':
                    v.color = 'gray'
                    v.d = u.d + 1
                    v.pi = u
                    Q.append(v)
            u.color = 'black'

if __name__ == '__main__':
    G = Graph()
    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    r.adj = [s, v]
    s.adj = [r, w]
    t.adj = [u, w, x]
    u.adj = [t, x, y]
    v.adj = [r]
    w.adj = [s, t, x]
    x.adj = [t, u, w, y]
    y.adj = [u, x]
    G.V = [r, s, t, u, v, w, x, y]
    m = Solution()
    m.BFS(G, s)
    for v in G.V:
        if v != s:
            print v.key, v.color, v.d, v.pi.key
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
                list=[u]
                self.DfsVisit(G, u, list)
                print ''.join([i.key for i in list])


    def DfsVisit(self, G, u, list):
        global time
        time = time + 1
        u.d = time
        u.color = 'gray'
        for v in u.adj:
            if v.color == 'white':
                list.append(v)
                v.pi = u
                self.DfsVisit(G, v, list)
        u.color = 'black'
        time = time + 1
        u.f = time

    def GraphTransposition(self, G):
        for u in G.V:
            u.adj = (u.adj,[])

        for u in G.V:
            for v in u.adj[0]:
                v.adj[1].append(u)

        for u in G.V:
            u.adj = u.adj[1]

        return G

    def StronglyConnectedComponents(self, G):
        self.Dfs(G)
        G_Transposition = self.GraphTransposition(G)
        G_Transposition.V.sort(key=lambda v: v.f, reverse=True)
        self.Dfs(G_Transposition)



if __name__ == '__main__':
    a,b,c,d,e,f,g,h = [Vertex(i) for i in ['a','b','c','d','e','f','g','h']]

    a.adj = [b]
    b.adj = [c,e,f]
    c.adj = [d,g]
    d.adj = [c,h]
    e.adj = [a,f]
    f.adj = [g]
    g.adj = [f,h]
    h.adj = [h]

    G = Graph()
    G.V = [a,b,c,d,e,f,g,h]

    m = Solution()
    m.StronglyConnectedComponents(G)
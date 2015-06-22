class Tree:
    def __init__(self):
        self.root = None

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def TreeSearch(self, x, k):
        if x == None or x.val == k:
            return x
        if k < x.val:
            return self.TreeSearch(x.left, k)
        else:
            return self.TreeSearch(x.right, k)

    def IterativeTreeSearch(self, x, k):
        while x != None and x.val != k:
            if k < x.val:
                x = x.left
            else:
                x = x.right
        return x

    def TreeMinimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def TreeMaximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def TreeSuccessor(self, x):
        if x.right != None:
            return self.TreeMinimum(x)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def TreeInsert(self, T, z):
        y = None
        x = T.root
        while x != None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            T.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right  = z

    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            print x.val
            self.InorderTreeWalk(x.right)

    def Transplant(self, T, u, v):
        if u.parent == None:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def TreeDelete(self, T, z):
        if z.left == None:
            self.Transplant(T, z, z.right)
        elif z.right == None:
            self.Transplant(T, z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            if y.parent != z:
                self.Transplant(T,y,y.right)
                y.right = z.right
                y.right.parent = y
            self.Transplant(T, z, y)
            y.left = z.left
            y.left.p = y


# root = TreeNode(15)
T = Tree()
nodes = [6,18,3,7,17,20,2,4,13,9]
s = Solution()
for node in nodes:
    s.TreeInsert(T,TreeNode(node))
s.InorderTreeWalk(T.root)
s.TreeDelete(T, T.root)
s.InorderTreeWalk(T.root)
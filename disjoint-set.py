class node(object):
	def __init__(self, val):
		self.val = val
		self.p = None
		self.rank = 0

def make_set(x):
	x.p = x
	x.rank = 0

def union(x, y):
	link(find_set(x), find_set(y))

def link(x, y):
	if x.rank > y.rank:
		y.p = x
	else:
		x.p = y
		if x.rank == y.rank:
			y.rank = y.rank + 1

def find_set(x):
	if x != x.p:
		x.p = find_set(x.p)
	return x.p

a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')
for node in [a,b,c,d,e,f]:
	make_set(node)

union(a,b)
union(c,d)
union(e,f)
union(a,c)
union(a,f)

for node in [a,b,c,d,e,f]:
	find_set(node)

for node in [a,b,c,d,e,f]:
	print node.p.val

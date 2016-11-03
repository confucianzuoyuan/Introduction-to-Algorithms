import heapq

def huffman(c):
    n = len(c)
    q = c[:]
    heapq.heapify(q)
    for i in range(n-1):
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        z = (x[0]+y[0], x[1]+y[1], x, y)
        heapq.heappush(q, z)
    return heapq.heappop(q)

c = [(45, 'a', None, None), (13, 'b', None, None), (12, 'c', None, None), \
     (16, 'd', None, None), (9, 'e', None, None), (5, 'f', None, None)]

print huffman(c)
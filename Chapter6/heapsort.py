class Heap(list):
	def __init__(self):
		list.__init__([])
		self.heap_size = 0

def parent(i):
	return i/2

def left(i):
	return 2*i

def right(i):
	return 2*i+1

def max_heapify(H, i):
	l = left(i)
	r = right(i)
	if l <= H.heap_size and H[l] > H[i]:
		largest = l
	else:
		largest = i
	if r <= H.heap_size and H[r] > H[largest]:
		largest = r
	if largest != i:
		H[i], H[largest] = H[largest], H[i]
		max_heapify(H, largest)

def build_max_heap(H):
	H.heap_size = len(H) - 1
	for i in range(len(H)/2,0,-1):
		max_heapify(H, i)

def heapsort(H):
	build_max_heap(H)
	for i in range(len(H)-1, 1, -1):
		H[1], H[i] = H[i], H[1]
		H.heap_size -= 1
		max_heapify(H,1)

if __name__ == "__main__":
	H = Heap()
	H += [0,9,8,7,6,5,4,3,2,1]
	heapsort(H)
	print H

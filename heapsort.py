class Heap(object):
	def __init__(self, length, heap_size):
		self.A = [0] * (length+1)
		self.length = length
		self.heap_size = heap_size

def parent(i):
	return i/2

def left(i):
	return 2*i

def right(i):
	return 2*i+1

def max_heapify(H, i):
	l = left(i)
	r = right(i)
	if l <= H.heap_size and H.A[l] > H.A[i]:
		largest = l
	else:
		largest = i
	if r <= H.heap_size and H.A[r] > H.A[largest]:
		largest = r
	if largest != i:
		H.A[i], H.A[largest] = H.A[largest], H.A[i]
		max_heapify(H, largest)

def build_max_heap(H):
	H.heap_size = H.length
	for i in range(H.length/2,0,-1):
		max_heapify(H, i)

if __name__ == "__main__":
	H = Heap(10,10)
	H.A = [0,16,4,10,14,7,9,3,2,8,1]
	max_heapify(H, 2)
	print H.A
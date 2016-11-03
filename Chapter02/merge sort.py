import sys

class mergesort():

    def merge_sort(self, A, p, r):
        if p < r:
            q = (p + r) / 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q+1, r)
            self.merge(A, p, q, r)
            return A

    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q

        L = [0 for i in range(n1+1)]
        R = [0 for i in range(n2+1)]

        for i in range(n1):
            L[i] = A[p+i]
        for j in range(n2):
            R[j] = A[q+j+1]

        L[n1] = sys.maxint
        R[n2] = sys.maxint

        i = 0; j = 0
        for k in range(p, r):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

sort = mergesort()

A = [1,3,5,7,9,2,4,6,8,10]

print sort.merge_sort(A, 0, len(A)-1)
# 直接寻址法

class HashTable:
    def __init__(self, length):
        self.T = [None for i in range(length)]

class Data:
    def __init__(self, key, satelite_data):
        self.key = key
        self.satelite_data = satelite_data

class Solution:
    def DIRECT_ADDRESS_SEARCH(self, T, k):
        return T[k]

    def DIRECT_ADDRESS_INSERT(self, T, x):
        T[x.key] = x

    def DIRECT_ADDRESS_DELETE(self, T, x):
        T[x.key] = None

# 分离连接法

class HashTable:
    def __init__(self, length):
        self.T = [None for i in range(length)]

class Data:
    def __init__(self, key, satelite_data):
        self.key = key
        self.satelite_data = satelite_data
        self.next = None

class Solution:
    def CHAINED_HASH_INSERT(self, T, x):
        '''insert x at the head of list T[h(x.key)]'''

        x.next = T[x.key].next
        T[x.key].next = x

    def CHAINED_HASH_SEARCH(self, T, k, satelite_data):
        '''search for an element with key k in list T[h(k)]'''

        tmp = T[k]
        while tmp.next.satelite_data != satelite_data:
            tmp = tmp.next

        return tmp

    def CHAINED_HASH_DELETE(self, T, x):
        '''delete x from the list T[h(x.key)]'''

        tmp = T[x.key]
        while tmp.next.satelite_data != x.satelite_data:
            tmp = tmp.next
        tmp.next = tmp.next.next

# 开放定址法

class HashTable:
    def __init__(self, length):
        self.T = [None for i in range(length)]

class Solution:
    def HASH_INSERT(self, T, k):
        i = 0
        m = len(T)
        while i < m:
            j = h(k, i)
            if T[j] == None:
                T[j] = k
                return j
            else:
                i = i + 1
        print "hash table overflow"

    def HASH_SEARCH(self, T, k):
        i = 0
        while True:
            j = h(k, i)
            if T[j] == k:
                return j
            i = i + 1
            if T[j] == None or i == m:
                break
        return None

    def h(self, k, i):
        '''linear probing'''

        return (k + i) % m
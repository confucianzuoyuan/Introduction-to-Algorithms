class insertionsort():

    def insertion_sort(self,Array):
        for i in range(1, len(Array)):
            key = Array[i]
            j = i - 1
            while j >= 0 and Array[j] > key:
                Array[j+1] = Array[j]
                j -= 1
            Array[j+1] = key

        return Array

sort = insertionsort()

array = [1,3,5,7,9,2,4,6,8,10]

print sort.insertion_sort(array)
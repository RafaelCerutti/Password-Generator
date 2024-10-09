
def bubbleSort(array):
    for i in range(len(array),0,-1):
        for j in range(0, i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]


array = [9,6,5,3,2,0,4,1,8,7]
bubbleSort(array)
print(array)
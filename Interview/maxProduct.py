import numpy as np
my_array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


def maxPod(arr):
    Product=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] * arr[j] > Product:
                Product= arr[i]*arr[j]
                pairs= str(arr[i]) +","+ str(arr[j])
    print(pairs)
    print(Product)


maxPod(my_array)
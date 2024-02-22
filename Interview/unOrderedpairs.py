def unOrderedpairs(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] < arr2[j]:
                print(arr1[i],arr2[j])



arrayA=[23,45,98,56,67,34,35,24,68,32]
arrayB=[56,72,23,83,46,34,76,35,78,45]

unOrderedpairs(arrayA,arrayB)
def reverse1(array):
    for i in range(0,int(len(array)/2)):
        start=array[i]
        array[i]=array[len(array)-i-1]
        array[len(array)-i-1]=start
    print(array)

arr=[1,2,3,4,5]
reverse1(arr)


def reverse2(array):
    print(array[::-1])

reverse2(arr)
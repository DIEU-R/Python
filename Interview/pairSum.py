def pairsum(lis,target):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i] + lis[j] == target:
                print ("targated sum index values : "+str(i)+","+str(j))



li=[1,2,3,4,5,6,23,2,45,2,3,35,2]
print(pairsum(li,6))
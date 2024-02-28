def missing_num(lis,num):
    sum1= (num*(num+1))/2
    sum2=sum(lis)
    miss_no= sum1-sum2
    return miss_no

li=[1,2,3,4,5,6,7,9,10]
print(missing_num(li,10))
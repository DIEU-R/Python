def podAndSum(array):
    sum=0
    product=1
    for i in array:
        sum += i

    for i in array:
        product*= i

    return ("sum = "+str(sum) +"\n"+ "product = "+str(product))



arr=[1,2,3,4,5]

print(podAndSum(arr))
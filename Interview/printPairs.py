def pp(arr):
    pairs=[]
    for i in arr:
        for j in arr:
            if i== j:
                pairs.append("bingo")
            else:
                pairs.append(str(i)+","+str(j))
    print(pairs)

array=[1,2,3,4,5]
pp(array)
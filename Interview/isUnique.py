my_list=[1,2,3,4,5,6,7,2,1,3,22,34,21,35,57]


def isUnique(list):
    temp=[]
    for i in list:
        if i in temp:
            print(i)
            return False
        else:
            temp.append(i)
    return True


print(isUnique(my_list))
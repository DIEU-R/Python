a=[1,2,3,7,8,3,3,4,4,6,6,9]
b=[1,3,4,7,3,6,9,3,6,8,4,2]

def permutation(lis1,lis2):
    if len(lis1) != len(lis2):
        return False
    lis1.sort()
    lis2.sort()
    if lis1 == lis2:
        return True
    else:
        return False
    

print(permutation(a,b))
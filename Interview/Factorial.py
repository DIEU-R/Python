def Fac(num):
    assert num>=0 and int(num)==num,"Then number should be integer only"
    if num ==0:
        return 1
    else:
        return num * Fac(num-1)
    

print(Fac(5))
def PowerOfTwo(n):
    if n==0:
        return 1
    else:
        power = PowerOfTwo(n-1)
        return power *2
    

print(PowerOfTwo(3))
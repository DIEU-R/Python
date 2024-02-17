def SumofDigits(n):
    assert n>=0 and int(n)== n,'The number has to be Positive integer only!'
    if n==0:
        return 0
    else:
        return int(n%10) + SumofDigits(n//10)
    

print(SumofDigits(1234))

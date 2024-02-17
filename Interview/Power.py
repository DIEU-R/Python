def power(base,exp):
    assert exp>=0 and int(exp) == exp,"The Exponent should be interger only!"
    if exp==0:
        return 1
    elif exp==1:
        return base
    return base * power(base,exp-1)




print(power(4,3))
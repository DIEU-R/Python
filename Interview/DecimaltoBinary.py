def DecimaltoBinary(n):
    assert int(n)==n ,"The number should be INTEGER only!"
    if n ==0:
        return 0
    else:
        return n%2 + 10*DecimaltoBinary(int(n/2))


print(DecimaltoBinary(1.3))
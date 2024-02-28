import statistics

def DAT2():
    tem=[]
    d_day=0
    days=int(input("Enter no of days : "))
    for i in range(1,days+1):
        temp = int(input("Enter day "+str(i)+"'s Temperature : "))
        tem.append(temp)
    Avg=round(statistics.mean(tem),2)
    print("Average Temperature : "+ str(Avg))
    
    for i in tem:
        if i>Avg:
            d_day += 1
    print("Days having Temperature above Average : "+ str(d_day))
    

DAT2()
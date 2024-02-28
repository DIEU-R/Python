# def Fib(num):
#     for i in range(num):
#         if num==0:
#             return 0
#         elif num==1:
#             return 1
#         return str(Fib(num-1)) + str(Fib(num-2))
        

# print(Fib(0))

def Fib(num):
    if (num==0 or num==1):
        return num
    return Fib(num-1) + Fib(num-2)


print(Fib(9))

def allFib(n):
    for i in range(n):
        print(str(i) +":, "+ str(fib(i)))


def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

print(allFib(5))

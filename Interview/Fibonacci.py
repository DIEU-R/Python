def Fibonacci1(n):
    for i in range(n):
        print(str(i+1) +":, "+ str(fib(i)))


def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

print(Fibonacci1(5))

def Fibonacci(num :int) -> int:
    match num:
        case 0 | 1:return num 
        case _ : return Fibonacci(num-1) + Fibonacci(num-2)


def Fibonacci2(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b=b,a+b

for n in Fibonacci2(10):
    print(n)
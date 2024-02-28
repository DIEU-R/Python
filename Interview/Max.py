li=[1,2,3,34,23,564,6,546,234,4,5,6]
def Max(list :list[int])->int|None:
    match list:
        case []: print("Plese Enter number ! list is Empty!!!") 
        case [x]: return x
        case [x,*x_rest] :return max(x,Max(x_rest))

print(Max(li))

a,c,*b=li
print(a,c,b)